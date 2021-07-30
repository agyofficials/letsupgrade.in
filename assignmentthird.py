'''Let's Upgrade Assignment 3rd'''
'''Submitted by Anurag Garg'''

'''
Consider a person is represented by Pi, where i is the index of the following list.
A list shows the person to whom person Pi has given the gift.
'''
#Solution 1st
print("Solution 1")
list = [2,1,5,3,4]
print("Check the person from whome gift is recieve\n")
personslist = list
print("Here are the person list",personslist)
var = int(input("Enter the number to check the gift person: "))
print() #Blank Line
if var == 1:
    print("P1 Got Gift From P2")
elif var == 2:
    print("P2 Got Gift From P1")
elif var == 3:
    print("P3 Got Gift From P5")
elif var == 4:
    print("P4 Got Gift From P3")
elif var == 5:
    print("P5 Got Gift From P4")
else:
    print("Wrong Input, Please enter the correct value / Number")

#Solution 2nd
print()
print("Solution 2")
print("Check the person from whome gift is recieved\n")
listRECEIVER= [2,1,5,3,4]
print("List the the RECEIVER",listRECEIVER)
x = 0
dict = {}
for i in listRECEIVER:
    x += 1
    dict[x] = i
listPRESENER = []
for x in range(1, len(list) + 1):
    for key, value in dict.items():
        if x == value:
            listPRESENER.append(key)
print("List of the PRESENER",listPRESENER)
#INPUT / OUTPUT
'''
letsupgrade.in/assignmentthird.py
Solution 1
Check the person from whome gift is recieve

Here are the person list [2, 1, 5, 3, 4]
Enter the number to check the gift person: 5

P5 Got Gift From P4

Solution 2
Check the person from whome gift is recieved

List the the RECEIVER [2, 1, 5, 3, 4]
List of the PRESENER [2, 1, 4, 5, 3]
'''