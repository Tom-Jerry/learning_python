# -*-coding: utf-8 -*-
'''
q1
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

q2
people = {
    'LiKexin':{
        'time':2012,
        'result':'fail',
    },

    'WangXiaoyi':{
        'time':2013,
        'result':'fail',
    },

    'HuangYiman':{
        'time':2015,
        'result':'win',
    },
}

for person, info in people.items():
    print('\n\t', person)
    for time, result in info.items():
        print('\t time:', time)
        print('\t result', result)

q3
pets = {
    'melie':{
        'type':'hasky',
        'owner':'german'
    },
    'rubert':{
        'type':'alaska',
        'owner':'german',
    },
    'xizhu':{
        'type':'samayh',
        'owner':'orange',
    },
}

for name, info in pets.items():
    print('\n\tname ', name)
    print('\ttype:',info['type'])
    print('\towner:',info['owner'])


#q4
favorite_places = {
    'fmr':['BeiJing', 'ChongQing', 'Chengdu'],
    'hym':['Chengdu', 'ChongQing'],
    'lkx':['BeiJing','Bristol'],
}
for name, places in favorite_places.items():
    print("\n\t" + name + "'s favorite places are:")
    for it in places:
        print("\t" + it)

#q5
cities = {
    'BeiJing':{
        'country':'china',
        'population':14,
        'fact':'capital',
    },
    'Bristol':{
        'country':'England',
        'population':0.1,
        'fact':'capital',
    },
    'Tokyo':{
        'country':'Japan',
        'population':0.1,
        'fact':'capital',
    },
}

for name, city in cities.items():
    print("\nname: " + name)
    print("city's location: " + city['country'])
    print("city's population: " + str(city['population']))
    print("city's fact: " + city['fact'])

prompt = "Please tell me what ingredents you want: "
completed = False
while completed ==  False:
    add = input(prompt)
    if add == "quit":
        completed = True
    else:
        print(add + "has been added!")

while True:
    age = input("\nquit to exit\nPlease enter your age: ")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("\nYou don't need to pay any coins")
    elif age >=3 and age <= 12:
        print("\nYou need to pay 10 dollars")
    else:
        print("\nYou need to pay 15 dollars")
'''
unconfirmed_users = ['alice', 'brain', 'cadance']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users has been confirmed:")
for user in confirmed_users:
    print("user: " + user.title())
