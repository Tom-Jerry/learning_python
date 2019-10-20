# -*-coding: utf-8 -*-
friend = {
    'first_name': 'yiman',
    'last_name': 'huang',
    'age':22,
    'city':'BeiJing'}

favorite_nums = {
    'Li': 1,
    'Wang': 2,
    'Xu':3,
    'Zhou': 4,
    'Huang': 5
}

words = {
    'C++': 'first',
    'Java': 'second',
    'Python': 'third'
}

for name, num in favorite_nums.items():
    print('key:',name, 'value:', num)
for key, value in words.items():
    print('key:',key, '\nvalue:', value)
