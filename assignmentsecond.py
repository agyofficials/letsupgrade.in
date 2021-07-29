'''Let's Upgrade Assignment 2nd'''
'''Submitted by Anurag Garg'''
#Question 1
#Delete all occurrences of an element in a list
#Creating a list.
list = []
x = int(input("Enter number of elements : ")) #Required Elements
for i in range(0, x): #Range illitration
            ele = int(input("Enter the Value's: "))
            list.append(ele) # adding the element
print("List Value in Order",list)

#deleting the occurence of a element/value
def removeVALUES(list, val):
   return [value for value in list if value != val]
rewise=list
element = int(input("Enter the element to delete: "))
rewise = removeVALUES(rewise, element)
print("Updated List Elements",rewise)

print()
print("Question 2")
#Question 2
#Check whether a string is a pangram.
#initializing
import string #importing modules
def isPANAGRAM(string, alphabets):
   for char in alphabets: # looping over the alphabets
      if char not in string.lower(): # if char not present in string
         return False ## return false
   return True
alphabets = string.ascii_lowercase #alphabets variable
stringONE = input("Enter First String, ") #String Initials ONE
#Sampleone - The Quick Brown Fox Jumps Over The Lazy Dog
stringTWO = input("Entre Second String, ") #String Initials TWO
#Sampletwo - letsupgradein
print("Yes Panagram") if isPANAGRAM(stringONE, alphabets) else print("Not Panagram")
print("Yes Panagram") if isPANAGRAM(stringTWO, alphabets) else print("Not Panagram")

#Sample INPUT/OUTPUT 
'''/letsupgrade.in/assignmentsecond.py
Enter number of elements : 10
Enter the Value's: 1
Enter the Value's: 2
Enter the Value's: 2
Enter the Value's: 3
Enter the Value's: 4
Enter the Value's: 5
Enter the Value's: 6
Enter the Value's: 8
Enter the Value's: 8
Enter the Value's: 8
List Value in Order [1, 2, 2, 3, 4, 5, 6, 8, 8, 8]
Enter the element to delete:2
Updated List Elements [1, 3, 4, 5, 6, 8, 8, 8]

Question 2
Enter First String, The Quick Brown Fox Jumps Over The Lazy Dog
Entre Second String, letsupgradein            
Yes Panagram
Not Panagram
'''