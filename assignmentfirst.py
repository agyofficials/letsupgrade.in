'''Let's Upgrade Assignment 1st'''
'''Submitted by Anurag Garg'''

#OTP GENERATOR USING PYTHON

import string
import random as r
length=6
otp=''
a = string.ascii_letters + string.digits
print(a)
for i in range(length):
  otp=otp+r.choice(a)
print("OTP: ",otp)
import string
import random as r
length=6
otp=''
a = string.ascii_letters + string.digits
print(a)
for i in range(length):
  otp=otp+r.choice(a)
print("OTP: ",otp)

#QUESTION 2

#Starting And Accepting User Input's
list = []
x = int(input("Enter number of elements : ")) #Required Elements
for i in range(0, x): #Range illitration
            ele = int(input("Enter the Value's: "))
            list.append(ele) # adding the element
print("List Value in Order",list)

#Shorting in Decending Order
list.sort(reverse = True)
print("List Value in Decending Order",list) #printing Values

#Sample Input/Output
'''
/letsupgrade.in/assignmentfirst.py
Enter number of elements : 5
Enter the Value's: 3
Enter the Value's: 1
Enter the Value's: 2
Enter the Value's: 4
Enter the Value's: 5
List Value in Order [3, 1, 2, 4, 5]
List Value in Decending Order [5, 4, 3, 2, 1]'''
