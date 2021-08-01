'''Let's Upgrade Final Project Submission'''
'''Submitted by Anurag Garg'''


#Question 1
'''Hey you are a chemist from India and you work with degree celsius in your day to day life but due to a project your company had collaborated with a MNC company, where the chemists use degree frainite for their purposes, and to maintain collaboration consistent we want to have a easy degree conversion,
Please develop a python based degree converter which takes °C value and give you output of °F'''

'''Input - 
°C -> 50
Output - 
°F -> 122 '''

#Propasal Program can accept both int() and float() values 
#Program can output/print in both int() and float() values

#Solution 1:
print("Tempreature Converter from Celcius to Farenheit\n")
cels=float(input("Enter the temperature in Celsius: "))
faren=(cels*9/5)+32
print("The Tempreature in Farenheit: ",int(faren))

#Solution 2 (More Accurate Result in Float)
faren=(float(cels)*9/5)+32
print("The Tempreature in Precise Farenheit: ",float(faren))

#Sample Input / Output
'''
/letsupgrade.in/finalproject.py
Tempreature Converterfrom Celcius to Farenheit

Enter the temperature in Celsius: 50
The Tempreature in Farenheit:  122
The Tempreature in Precise Farenheit:  122.0

Enter the temperature in Celsius: 50.54
The Tempreature in Farenheit:  122
The Tempreature in Precise Farenheit:  122.97200000000001'''
