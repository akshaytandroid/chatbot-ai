import aiml
import os, fnmatch
import sys


bot=aiml.Kernel()
aimldir = os.path.join(sys.path[0], "aimlfiles")
aimldir = aimldir.replace("library.zip\\","")
pattern="*.aiml"
print "Looking for aiml files in %s ..." % aimldir

for path, dirs, files in os.walk(os.path.abspath(aimldir)):
        for filename in fnmatch.filter(files, pattern):
            newfile= os.path.join(path, filename)
            bot.learn(newfile)


#bot.learn("Computers.aiml")
while True: print bot.respond(raw_input("> "))




