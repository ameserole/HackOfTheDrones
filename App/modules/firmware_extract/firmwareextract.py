#!/usr/bin/python3
import os
import subprocess



class firmwareExtract():
    def __init__(self, filename):
        self.current_level = 0
        os.system("rm -rf tmp*/" )

        self.filename = filename
        #unzip_process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
        #output = unzip_process.communicate()[0]
        #print (output.decode('ascii'))
    def getMagic(self, filename):
        fd = open(filename, "rb")
        data = fd.read(2)
        print ("%x %x: %s" % (data[0], data[1], data.decode('ascii')))
        fd.close()
        return data.decode('ascii')



    def deflate(self, filename):
        if self.getMagic(filename) == "PK":
            level_used = self.current_level
            print("[!] We Have a ZIP")
            os.system("mkdir tmp%d" % self.current_level)
            os.system("unzip %s -d tmp%d/" % (filename, self.current_level))
            unzip_process = subprocess.Popen(["ls", "tmp%d/" % self.current_level], stdout=subprocess.PIPE)
            output = unzip_process.communicate()[0]
            output = output.decode('ascii')
            print (output)
            self.current_level += 1
            return (level_used, output.split("\n"))
        else:
            file_type_process = subprocess.Popen(["file","%s" % (filename)], stdout=subprocess.PIPE)
            output = file_type_process.communicate()[0]
            output = output.decode('ascii')
            print (output)
            if output.find(": data") != -1:
                print ("[!] We have a data blob!!")
            os.system("binwalk -e %s" % filename)
            return (None, [])
        print("[!] File Magic Not Found")
        return (None, [])

    def deflate_list(self, filename_list, used_level):
        for afile in filename_list:
            print ("[!] Trying to extract: %s" % afile)
            if afile == '':
                continue

            print(fe_obj.getMagic("tmp%d/%s" % (used_level, afile)))
            print("!!!!")
            print (used_level)
            print(afile)
            print("tmp%d/%s" % (used_level, afile))
            lvl, files = fe_obj.deflate("tmp%d/%s" % (used_level, afile))
            if len(files) > 0:
                self.deflate_list(files, lvl)

    def save_extracted(self, dest_folder):
        for i in range(0, self.current_level):
            unzip_process = subprocess.Popen(["ls", "tmp%d/" % i], stdout=subprocess.PIPE)
            output = unzip_process.communicate()[0]
            output = output.decode('ascii').split("\n")
            print (output)
            for afolder in output:
                if afolder.find(".extracted") != -1:
                    print ("[!] We Have an extracted folder")
                    os.system("cp -r tmp%d/%s %s" % (i, afolder, dest_folder))


    def run(self, outfolder):
        used_level, extracted_files = fe_obj.deflate(self.filename)
        fe_obj.deflate_list(extracted_files, used_level)
        fe_obj.save_extracted(outfolder)



#fe_obj = firmwareExtract('/root/Desktop/TyphoonH_Ver3.04_A.bin')
#used_level, extracted_files = fe_obj.deflate(fe_obj.filename)


#print (fe_obj.current_level)
#fe_obj.save_extracted("datastore")


