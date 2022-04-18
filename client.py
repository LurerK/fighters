import numpy as np


userInput=input("Type 1 to Upload a file or type 2 to enter fighters manually:")
if (userInput==1):
    fileName=input("what file: ")
    print("Username is: " + username)
    fileText = open('name.txt', ' r')
    fileRead = fileText.readlines()
    for i in fileRead:
        print("{}".format(fileRead.strip())
        
    fileText.close
elif(userInput==2):
    size=input("How many fighters")
    for i in np.array[size][3]:
        charName=input("")
        char=
else: