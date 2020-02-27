#######################################
### Andrew Poole                    ###
### AIST 2120                       ###
### Programming Assignment 4 Part I ###
### 10/15/2019                      ###
### regexinatorplus.py              ###
#######################################
###*********************************###
import pyperclip, re, zipfile, os #imports the modules

#Creating phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|.)
    (\d{3})
    (\s|-|.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)   #compiles phone number format
                        #so it knows what to look for
#Creating email regex
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+=]+
    @
    [a-zA-Z0-9.-]+
     (\.[a-zA-Z]{2,4})
     )''', re.VERBOSE)   #compiles email format
                        #so it knows what to look for
matches=[]#creates empty list of matches
print("Welcome to Phone and Email Extractor!")#welcomes the user
searchy = input("Please enter a file name: ")#asks for input file
openy = open(searchy,'r')#opens the file inputted
text = openy.read()#reads the file to use later

for groups in phoneRegex.findall(text):#finds all regex links
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])#finds phone
    if groups[8] != '': #makes sure the numbers are the right amount
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):#and then it does the same
    matches.append(groups[0])#for phone numbers
openy.close()#closes file

if len(matches) > 0:#if theres more than zero matches...
    pyperclip.copy('\n'.join(matches))#it copies the matches listed
    openz = open('output.txt','w')#to output.txt
    openz.write(pyperclip.paste())
    openz.close()
else:
    print('No phone numbers or email addresses found.')
                             #otherwise it prints this

newZip = zipfile.ZipFile('output.zip','w')#creates zip
newZip.write('output.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()#copies output.txt to .zip and closes zip
