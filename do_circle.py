# -*- coding: utf-8 -*-
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me sth, and I'll repeat it back:"
prompt += "\nEnter 'quit' to exit."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message) 

prompt = "\nTell me sth, and I'll repeat it back:"
prompt += "\nEnter 'quit' to exit."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

'''