
import os
import shutil

##directorypath = r"Path_To_Files"
directoryPath = r"W:\Airphotos\2015\TIF_Summer"
containerDirectory = directorypath + "\\TIFF\\"

# Add any extensions you want copied. Remove those you don't want copied
extensions = [".tif",".aux",".rrd",".tfw","f.xml","f.ovr","x.xml"]

#Loop through all subfolders in your target directory. Find each map document and replace the workspace paths. Remember to enter your own workspace path below.



def copyFiles():
      for f in os.listdir(directoryPath):
            directoryName = containerDirectory + f[:4]
            src = directoryPath + "\\" + f
            srcFileName = os.path.basename(src)
            if ((not os.path.isfile(directoryName + "\\" + srcFileName)) and (f[-4:].lower() in extensions) or (f[-5:].lower() in extensions)):
                  print "copying " + srcFileName
                  shutil.copy2(src, directoryName)
            else:
                  pass
      print "Finished copying files"

#Search a directory for the first four digits of a file name and create subdirectories with the four digits as the names
def createDirs():
      mylist = []
      for f in os.listdir(directorypath):
            print f
            f = f[:4]
            if f.startswith('2') or f.startswith('3'):
                  print f
                  mylist.append(f)
                  print len(mylist)
                  if not os.path.exists(tifpath + f):
                      os.makedirs(tifpath + f)

