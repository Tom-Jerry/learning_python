#-*- coding: utf-8 -*-
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

print("Give me two numbers and I'll divide them.")
print("Enter q to quit.")

while True:
    first_number = input("Please enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Please input the second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)

filename = 'alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    #msg = "Sorry the file is not found!"
    #print(msg)
    pass
else:
    words = contents.split()
    num_words = len(num_words)
    print("The file: " + filename + " contains " + num_words + " words.")


print("Enter q to exit.")
while True:
    try:
        num1 = input("Please enter a number: ")
        if num1 == 'q':
            break
        num1 = int(num1)
    except ValueError:
        #msg = "What you entered is not a number!"
        #print(msg)
        continue
    else:
        try:
            num2 = input("Please enter a number again: ")
            if num2 == 'q':
                break
            num2 = int(num2)
        except ValueError:
            #msg = "What you entered is not a number!"
            #print(msg)
            continue
        else:
            answer = num1 + num2
            print(answer)


try:
    with open('dogs.txt') as dog:
        dog_contents = dog.readlines()
except FileNotFoundError:
    #msg = "Can't find the file dogs"
    #print(msg)
    pass
else:
    try:
        with open('cats.txt') as cat:
            cat_contents = cat.readlines()
    except FileNotFoundError:
        #msg = "Can't find the file cats"
        #print(msg)
        pass
    else:
        for line in dog_contents:
            print("dog: " + line.rstrip() + ".")
        for line in cat_contents:
            print("cat: " + line.rstrip() + ".")

'''

