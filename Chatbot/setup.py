from distutils.core import setup
import os, fnmatch
import sys
import py2exe
import shutil

setup(console=['chatbot.py'])
pattern="*.aiml"
aimldir = os.path.join(sys.path[0], "aimlfiles")

for path, dirs, files in os.walk(os.path.abspath(aimldir)):
        for filename in fnmatch.filter(files, pattern):
            newfile= os.path.join(path, filename)
            if not os.path.exists("%s\\dist\\aimlfiles" % sys.path[0]):
                os.mkdir("%s\\dist\\aimlfiles" % sys.path[0])
            dst = "%s\\dist\\aimlfiles\\%s" % (sys.path[0],filename)
            shutil.copyfile(newfile, dst)
