#-*- coding: utf-8 -*-
import json

'''
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'a') as f:
    json.dump(numbers, f)

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)


filename = 'user.json'
print("Enter q to exit")
while True:
    username = input("What is your name? ")
    if username == 'q':
        break
    with open(filename, 'w') as f:
        json.dump(username,f)
        print("We'll remember you when you are back " + username + ".")


filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Enter a username: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("The user name has been saved")
else:
    print("Welcomback " + username + " ! ")

'''


def save_number(number, filename):
    """将参数中指定的数字，存入指定文件,并将存入的数字作为返回值返回"""
    try:
        with open(filename, 'a') as f:
            json.dump(number, filename)
    except FileNotFoundError:
        return False
    else:
        return True

def show_number(filename):
    """打开参数指定的文件， 并将读取到的数字进行输出展示
    如果，存储文件不存在则返回None，存在则返回名称"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

info = show_number('username.json')
if info:
    print("user name: " + info)
else:
    name = input("Please enter a name.")
    res = save_number(name, 'username.json')
    if res:
        print("success")
    else:
        print("defeat")
