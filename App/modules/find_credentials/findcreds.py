import os
import re
import sys
import argparse


outfile = None

'''
' Scan through a single file line by line.
' Check for common password and hash formats.
' Returns a list of password and/or hash formats found in the file.
'''
def scanFile(directory, expression, outfile):
    #If the file exists, scan it
    if os.path.exists(directory):
        #like my regex expression? It's okay...
        exp = re.compile(expression, re.IGNORECASE)

        lines = []

        with open(directory) as fp:
            try:
                line = fp.readline()
                cnt = 1
                while line:
                    matches = exp.findall(line)
                    if len(matches) >= 1:
                        lines.append("\t{}: {}".format(cnt, line.strip()))
                    line = fp.readline()
                    cnt+=1
            except UnicodeDecodeError:
                #It's a binary file, do nothing
                None

        if len(lines) >= 1:
            filename = os.path.basename(directory) + ":"
            if outfile is not None:
                f=open(outfile, 'a')
                f.write(filename + "\n")
                f.close()
            else:
                print(os.path.basename(directory) + ":")

            for line in lines:
                if outfile is not None:
                    f=open(outfile, 'a')
                    f.write(line + "\n")
                    f.close()
                else: print(line)
    else: print("WARNING: " + os.path.basename(directory) + " file does not exist!")

'''
'   Searches through the firmware file structure to find default credentials.
'   Automatically pulls /etc/shadow and /etc/webpass.txt files if they exist
'''
def findcreds(directory, searchAll, expression, outfile):
    expstr = "using expression: " + repr(expression)
    if outfile is not None:
        f=open(outfile,'a')
        f.write(expstr + "\n")
        f.close()
    else:
        print(expstr)

    #Pull files we know of that have jucy information
    scanFile(directory + "/etc/shadow", expression, outfile)
    scanFile(directory + "/etc/webpass.txt", expression, outfile)
    scanFile(directory + "/etc/init.d/S90", expression, outfile)
    
    #   Scan through entire file structure to find potential credentials
    if searchAll == True:
        for root, dirs, files, in os.walk(directory):
            path = root.split(os.sep)
            for file in files:
                #Go through file line by line and check for potential matches to cred formats
                scanFile(os.path.abspath(root) + '/' + file, expression, outfile)

'''
' If this module is running on its own, parse the command line arguments for it
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='scan firmware for default credentials.')
    parser.add_argument('firmware_directory', type=str, help='root directory of the firmware')
    parser.add_argument('-s', '--scanAll', help="scan the entire file structure", action="store_true")
    parser.add_argument('-o', '--outfile', type=str, help="output file for found credentials")
    parser.add_argument('-e', '--regex', type=str, help="input a custom regex expression, use this instead of the default")
    
    args = parser.parse_args()
    if args.regex is None:
        args.regex = '(((passw(or)?d)|(passphrase)|(pass)|(key)) *[:=] *.*)|(^[#]?\w+:[^\n]*)' 
    findcreds(args.firmware_directory, args.scanAll, args.regex, args.outfile)
