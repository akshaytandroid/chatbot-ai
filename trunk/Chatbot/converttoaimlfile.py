from xml.dom.minidom import Document
from Database import Database


structmonth=['january', #0
            'february',#1
            'march',#2
            'april',#3
            'may',#4
            'june',#5
            'july',#6
            'august',#7
            'september',#8
            'october',#9
            'november',#10
            'december']#11

hostEPquestions = [ 'WHO HOST EPISODE <ep>', 'WHO HOSTED EPISODE <ep>', 'WHO WAS THE HOST ON EPISODE <ep>', 'WHO HOSTED ON EPISODE <ep>' ]

hostMSquestions = ['WHO WAS MUSICAL GUEST WHEN <host> HOSTED',
                   'WHO WAS THE MUSICAL GUEST WHEN <host> HOSTED',
                   'WHEN <host> HOSTED WHO WAS THE MUSICAL GUEST',
                   'WHEN <host> HOSTED WHO WAS MUSICAL GUEST',
                   'WHEN <host> HOSTED WERE MUSICAL GUESTS',
                   'WHEN <host> HOSTED WHO WERE MUSICAL GUESTS',
                   'WHEN <host> HOSTED WHO WERE THE MUSICAL GUESTS']

hostdatequestions =  ['WHEN * <host> HOST',
                      'WHAT DATE DID <host> HOST',
                      'WHAT DATE DID <host> HOST * ',
                      'WHAT AIRDATE DID <host> HOST',
                      'WHAT AIR DATE DID <host> HOST']



def createaimlfile(currentdb):
    # Create the minidom document
    doc = Document()
    # Create the aiml base element
    aiml = doc.createElement("aiml")
    doc.appendChild(aiml)
    currenthost=""
    currentdb.sort_host()
    for show in currentdb.show_list:
        if show.host not in currenthost:
            strguests=""
            currenthost = show.host

        for guest in show.musicalguest:
            if len(strguests) == 0:
                strguests = guest + " on show number " + str(show.epnumber).upper()
            else:
                strguests += ", " + guest + " on show number " + str(show.epnumber).upper()
                
        for ep in hostEPquestions:
            strqu = ep.replace('<ep>',str(show.epnumber).upper())
            # Create category element
            maincard = doc.createElement("category")
            aiml.appendChild(maincard)

            # pattern
            pattern = doc.createElement("pattern")
            maincard.appendChild(pattern)
            # pattern text
            ptext = doc.createTextNode(strqu)
            pattern.appendChild(ptext)

            # template 
            template = doc.createElement("template")
            maincard.appendChild(template)
            # template text
            strhost = show.host
            if "(none)" in strhost:
                strhost="No one"
            ptext = doc.createTextNode(strhost)
            template.appendChild(ptext)

        for mg in hostMSquestions:
            strhost = str(show.host).upper()
            if "(none)" in strhost:
                strhost="No one"
            strqu = mg.replace('<host>',strhost)
            # Create category element
            maincard = doc.createElement("category")
            aiml.appendChild(maincard)

            # pattern
            pattern = doc.createElement("pattern")
            maincard.appendChild(pattern)
            # pattern text
            ptext = doc.createTextNode(strqu)
            pattern.appendChild(ptext)

            # template 
            template = doc.createElement("template")
            maincard.appendChild(template)
            # template text
            ptext = doc.createTextNode(strguests)
            template.appendChild(ptext)

        for da in hostdatequestions:
            strhost = str(show.host).upper()
            if "(none)" in strhost:
                strhost="No one"
            strqu = da.replace('<host>',strhost)
            # Create category element
            maincard = doc.createElement("category")
            aiml.appendChild(maincard)

            # pattern
            pattern = doc.createElement("pattern")
            maincard.appendChild(pattern)
            # pattern text
            ptext = doc.createTextNode(strqu)
            pattern.appendChild(ptext)

            # template 
            template = doc.createElement("template")
            maincard.appendChild(template)
            # template text
            stryear = str(show.airdate)[0:4]
            strmon = str(show.airdate)[4:6]
            strday = str(show.airdate)[6:8]
            strmon = structmonth[int(strmon)-1]
            numlen = len(strmon)
            strmon = strmon[0:1].upper() + strmon[1:numlen]
            strairdate = "%s %s, %s" % (strmon,strday,stryear)
            ptext = doc.createTextNode(strairdate)
            template.appendChild(ptext)



    filename ='C:\\Users\\Shaffer\\Desktop\\School\\A.I\\chatbot-ai\\trunk\\Chatbot\\aimlfiles\\snl.aiml'
    newfile = open(filename,'w')
    newfile.write(doc.toprettyxml(indent="  "))
    newfile.close()
    #print doc.toprettyxml(indent="  ")

CurrentDatabase = Database("snl.dat")
createaimlfile(CurrentDatabase)

