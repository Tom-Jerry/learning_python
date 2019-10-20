#-*- coding: utf-8 -*-
'''
message = input("Tell me sth, and I will repeat it to you ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are,"
prompt += "we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("You are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you are a little older.")

number = input("Enter a number and I will tell you if it's even od odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

car_type = input("Please tell me what kind of car you want: ")
print("Let me see if I can find you a " + car_type)
'''

count = input("Please tell me how many people you are: ")
count = int(count)
if count > 8:
    print("There is no table for you.")
else:
    print("Here is a table.")