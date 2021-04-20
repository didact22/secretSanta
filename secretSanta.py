#Assign 5 different names to 5 different people, then email the results

import smtplib
import random

def secretSanta():
    # this code block assigns the names randomly
    #oList is the list im not changing(original list)
    oList = ["name1","name2","name3","name4","name5"]
    #nList gets changed and then compared against oList to look for same name assignments.
    #oList is the person, nList is their assignment 
    nList = ["name1","name2","name3","name4","name5"]
    #dictionary to allow for email lookups
    nameDict = {"name1": "name1 EMAIL ADDRESS", "name2": "name2 EMAIL", "name3":"name3 EMAIL", "name4":"name4 EMAIL", "name5":"name5 EMAIL"}
    #shuffle the nList randomly
    random.shuffle(nList)
    #a good match is when each name(from the different lists) at the same index is different
    goodMatch = False
    while (goodMatch == False):
        if (checkForSame(nList,oList) == 1): # if its not a valid arrangement, shuffle again
            random.shuffle(nList)
        elif (checkForSame(nList,oList) == 0):
            goodMatch = True
    #oList is the person, nList is their assignment 
    for x in oList:
        mail = nameDict[x]
        name = nList[oList.index(x)]
        sendEmail(name,mail) 
        #print(name + " is getting sent to " + mail) comment out the above line and un comment this line to debug matches/ to not send mail and just observe the outcomes. 


def sendEmail(nam, mail):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("YOUR GMAIL ADDRESS GOES HERE","YOUR GMAIL PASSWORD GOES HERE")
    msg = "You are secret santa for " + name
    server.sendmail("YOUR GMAIL ADDRESS GOES HERE",email, msg)
    server.quit()


def checkForSame(list1,list2):
    num = 0 
    while (num < 5):
        if (list1[num] == list2[num]): 
            return 1
        else:
            num +=1
    return 0 


secretSanta()
