"""
stringjumble.py
Author: Liam S
Credit: Stack Overflow to learn what .join could do.

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
inputString = str(input("Please enter a string of text (the bigger the better): "))
print('You entered "' + inputString + '". Now jumble it:')
firstList = list(inputString)

secondList = firstList[::-1]
print("".join(secondList))
testList = []
counter = len(firstList)
counter2 = len(firstList)
while counter > -1:
    counter -= 1
    if firstList[counter] == ' ':
        testList.append("".join(firstList[counter:counter2]))
        counter2 = counter
testList.append(' ')
testList.append("".join(firstList[:counter2]))
print("".join(testList))

thirdList = firstList[::-1]
test2List = []
counter3 = len(firstList)
counter4 = len(firstList)
while counter3 > -1:
    counter3 -= 1
    if thirdList[counter3] == ' ':
        test2List.append("".join(thirdList[counter3:counter4]))
        counter4 = counter3
test2List.append(' ')
test2List.append("".join(thirdList[:counter4]))
print("".join(test2List))