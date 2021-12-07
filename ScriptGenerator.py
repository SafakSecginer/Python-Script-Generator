from os import walk
import shutil

#For read content and check the variables
def readContent():

    f = [] #File list

    for (dirpath, dirnames, filenames) in walk("template"): #We check template folder for dirpath, dirnames, filenames

        f.extend(filenames) #We added the filenames to the f (file list)

        break

    fileNumber = 0

    #If we want read contents and print them to the console...

    for i in f:

        fileNumber += 1

    print("\n------------------------------")

    return [fileNumber,filenames]

def editScript(IN, target,LEN, fileNumber, filenames):

    if LEN == 0: #We look for the input

        fileNumberForLoop = 1

        for name in filenames:

            print("[{}] {}".format(fileNumberForLoop, name))

            if ((fileNumberForLoop -1) < fileNumber):

                fileNumberForLoop += 1

        try:

            scriptNumberForChange = int(input("Please Enter A File Number: "))

        except ValueError:

            print("Please Enter An Existing Number!")

        newScriptName = input("Enter New Script Name: ")

        src = "template\{}".format(filenames[scriptNumberForChange - 1])

        dst = "output\{}".format(newScriptName)

        shutil.copyfile(src, dst)

    else:

        src = "template\{}".format(IN)

        dst = "output\{}".format(target)

        shutil.copyfile(src, dst)



print("---------------------------------------------------")
print("Welcome and thanks for your determination!")
print("For Exit, Please Press 'q' ")
print("---------------------------------------------------")

source = str

while(True):

    IN = input()

    if IN == 'q':

        break

    if len(IN) == 0:

        #If we want to read contents in the scripts...
        value = readContent() #value contains number of scripts and script names.

        try:
            editScript("", "",0,value[0], value[1])

        except IndexError:

            print("Please Enter An Existing Number!")

        except UnboundLocalError:

            continue

    else:

        value = readContent()

        b = IN.split()

        try:

            source = b[0]

        except IndexError:

            print("Please do not enter words that only contain spaces.")


        try:

            target = b[1]

        except IndexError:

            print("Please enter two words with a space in between.")

        if (source in value[1]): #We inquired whether the entered name exists.

            try:

                editScript(source, target,1, value[0], value[1])

            except NameError:

                print("Please enter the target file name.")

        else:

            print("There Is No Script File Like This!")










