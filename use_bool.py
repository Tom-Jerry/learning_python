#-*- coding:utf-8 -*-
prompt = "\nTell me sth and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)