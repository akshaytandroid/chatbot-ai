import aiml
import os, fnmatch
import sys


bot=aiml.Kernel()
aimldir = os.path.join(sys.path[0], "aimlfiles")
aimldir = aimldir.replace("library.zip\\","")
pattern="*.aiml"
print "Looking for aiml files in %s ..." % aimldir

x=0
for path, dirs, files in os.walk(os.path.abspath(aimldir)):
        matlist =fnmatch.filter(files, pattern)
        for filename in matlist:
            newfile= os.path.join(path, filename)
            x+=1
            bot.learn(newfile)
print "Loaded %s files" % x
print '-'*80
            
while True:
        strinput = raw_input("> ")
        if 'exit' in strinput.lower():
                sys.exit(0)
        strreturn= bot.respond(strinput)
        print strreturn
   
                




