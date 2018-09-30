from collections import namedtuple
from datetime import datetime, timezone
import logging
import re
import xml.etree.cElementTree as ET

logger = logging.getLogger(__name__)

GpsRecord = namedtuple('GpsRecord', ['timestamp', 'altitude', 'latitude', 'longitude'])

NS_GPX = 'http://www.topografix.com/GPX/1/1'
GPX_TEMPLATE = '<gpx xmlns="{}" version="1.1" />'.format(NS_GPX)
ET.register_namespace('', NS_GPX)

TIMESTAMP_FORMAT = re.compile(r'^(?P<Y>\d{4})(?P<M>\d{2})(?P<D>\d{2}) (?P<h>\d{2}):(?P<m>\d{2}):(?P<s>\d{2}):(\d{3})$')

def parse_time(timestamp):
    match = TIMESTAMP_FORMAT.match(timestamp)
    if not match:
        raise ValueError('Invalid timestamp: {}'.format(timestamp))

    year = int(match.group('Y'))
    month = int(match.group('M'))
    day = int(match.group('D'))
    hour = int(match.group('h'))
    minute = int(match.group('m'))
    second = int(match.group('s'))

    return datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)

def to_gpx(records, title='GPS log'):
    xml_root = ET.fromstring(GPX_TEMPLATE)
    xml_track = ET.SubElement(xml_root, 'trk')
    xml_name = ET.SubElement(xml_track, 'name')
    xml_name.text = title
    xml_segment = ET.SubElement(xml_track, 'trkseg')
    for record in records:
        xml_waypoint = ET.SubElement(xml_segment, 'trkpt', lat=record.latitude, lon=record.longitude)
        xml_elevation = ET.SubElement(xml_waypoint, 'ele')
        xml_elevation.text = record.altitude
        xml_time = ET.SubElement(xml_waypoint, 'time')
        xml_time.text = record.timestamp.isoformat()

    return ET.tostring(xml_root, encoding='unicode')

def parse_yuneec_log_str(in_str, skip_headers=True):
    records = []

    lines = in_str.splitlines()
    if skip_headers:
        lines = lines[1:]

    num_skipped = 0

    for line in lines:
        cols = line.strip().split(',')
        if len(cols) < 6:
            logger.error('malformed row: skipping record...')
            num_skipped += 1
            continue

        try:
            timestamp = parse_time(cols[0])
        except ValueError:
            logger.exception('Unable to parse datetime: skipping record...')
            num_skipped += 1
            continue

        alt = cols[3]
        lat = cols[4]
        lng = cols[5]

        record = GpsRecord(timestamp, alt, lat, lng)
        records.append(record)

    if num_skipped > 0:
        num_total = len(lines)
        num_success = num_total - num_skipped
        logger.error('Parsed {0} out of {1} record(s): {2} record(s) were skipped due to errors.'.format(num_success, num_total, num_skipped))

    return records

def yuneec_to_gpx(in_str, skip_headers=True, title='GPS log'):
    return to_gpx(parse_yuneec_log_str(in_str, skip_headers), title)
