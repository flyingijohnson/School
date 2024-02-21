# This is a Mad Libs program that reads in text files and lets the user add their own 
# text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Module 4 Assignment 2
# Ian Johnson

import re
import pyinputplus as pyip

# Change the following variable to the neccessary file destination.
# Be sure to use the absolute path, not the relative path.
# Also make sure to escape any characters neccessary
fileDestination = 'C:\\Users\\ianjj\\OneStop\\Repos\\School\\TextFiles\\'

# Change the following variable to the text file name to read:
fileName = "MadLibs.txt"

#START OF PROGRAM

# Open the Mad Libs file and put the text to a variable:
madLibs = open((fileDestination + fileName), 'r')
madLibText = madLibs.read()
madLibs.close()

# Check the text for the mad libs
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

# Put the results into a list
result = check.findall(madLibText)

# Replace the madlib with a word that fits.
# This will allow for numbers as well, but I don't know how to get around that.
for word in result:
    if word == "ADJECTIVE":
        userInput = pyip.inputStr("Enter an ADJECTIVE: ")
        madLibText = re.sub(word, userInput, madLibText, count = 1)
    elif word == "NOUN":
        userInput = pyip.inputStr("Enter a NOUN: ")
        madLibText = re.sub(word, userInput, madLibText, count = 1)
    elif word == "VERB":
        userInput = pyip.inputStr("Enter a VERB: ")
        madLibText = re.sub(word, userInput, madLibText, count = 1)
    elif word == "ADVERB":
        userInput = pyip.inputStr("Enter an ADVERB: ")
        madLibText = re.sub(word, userInput, madLibText, count = 1)

# print the result to the terminal:
print(madLibText)

# pick a new file name.
newFileName = input("Name your new file. Remember to add .txt to the end:")

# Writes the output to a new file:
new_file = open((fileDestination + newFileName), "w")
new_file.write(madLibText)
new_file.close()
