#-*- coding: utf-8 -*-
'''
filename = 'pi_digits.txt'

pi_str = ""
with open(filename) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    pi_str += line.rstrip()

birthday = input("Please enter your birthday: ")
if birthday in pi_str:
    print("Yes")
else:
    print("No")

filename = "guest.txt"
with open(filename, 'a') as file_obj:
    print("yes/no-------continue/breakout")
    while True:
        name = input("Please enter your name:")
        if name == 'exit':
            break
        else:
            reason = input("Why you love programming? ")
            print("hello " + name + ".")
            file_obj.write("\n")
            file_obj.write(name)

'''

filename = 'note.txt'
with open(filename, 'a') as f:
    while True:
        reason = input("Why you love programming?")
        if reason == "exit":
            break
        else:
            f.write('\n')
            f.write(reason)