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


unconfirmed_users = ['alice', 'brain', 'cadance']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users has been confirmed:")
for user in confirmed_users:
    print("user: " + user.title())

pets = ['dog', 'cat', 'goldfish', 'rabbit', 'cat', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}
goon = True
while goon:
    name = input("Please enter your name:")
    response = input("What's your favorite mountain:")

    responses[name] = response

    ask = input("Let the next one answer the questions?(yes or no)")
    if ask == 'no':
        goon = False
    
print("results:")
for name, response in responses.items():
    print("name: " + name + " mountain: " + response)

sandwich_orders = ['tuna', 'pastrami','fish', 'chicken', 'pastrami','beef','pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("There is no pastrami on sell")


result = {}
still = True
while still:
    name = input("What's your name:")
    answer = input("Where is your favorite place for vacation:")
    result[name] = answer
    judge = input("next one (yes or no)?")
    if judge == 'no':
        still = False

for n, p in result.items():
    print("name: " + n + " vacation: " + p) 

def make_shirt(size='L', picture='default'):
    print("Thirt's size:    " + str(size))
    print("Thirt's picture: " + str(picture))
make_shirt()
make_shirt('M')
make_shirt('S', 'others')

def describe_city(name, nation='China'):
    print("\ncity:    " + name)
    print("nation:  " + nation)

describe_city('Reykjavik', 'Iceland')
describe_city('Bristol', 'England')
describe_city('BeiJing')

def make_album(singer, name_album,count):
    result = {}

    result['singer'] = singer
    result['name'] = name_album
    result['count'] = count

    return result

print(make_album('Jay Chou', 'fantasy',7))


def make_great(name):
    res = []
    for n in name:
        n = n + " the Great"
        res.append(n)
    return res
def show_magic(name):
    print()
    name = make_great(name)
    for n in name:
        print("magician name: " + n)
show_magic(['lkx','wxy','hym'])

def make_car(producer, num, **others):
    car_info = {}
    car_info['producer'] = producer
    car_info['num'] = num
    for key, value in others.items():
        car_info[key] = value
    return car_info

new_car = make_car('subaru', 'outback', color='blue', package='two')
print(new_car)

class Restaurant():
    def __init__(self, restaurant_name, restaurant_type,
        number_served=0):
        self.restaurant_name =  restaurant_name
        self.restaurant_type =  restaurant_type
        self.number_served = number_served
    
    def set_number_served(self,value):
        self.number_served = value
    
    def increment_number_served(self,increment):
        self.number_served += increment

    def describe_restaurant(self):
        print("\nRestaurant name: " + self.restaurant_name)
        print("Restaurant type: " + self.restaurant_type)
        print("Restaurant has served " + str(self.number_served) + " persons")
    def open_restaurant(self):
        print("\nNow the restaurant is on !")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, restaurant_type,number_served=0):
        super().__init__(restaurant_name, restaurant_type, number_served)
        self.flavors = ['lemon', 'milk', 'orange']
    def describe_icecream(self):
        print("The tastes of our icecream: " + str(self.flavors))
 
class User():
    def __init__(self, first_name, last_name,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("\nuser info " + self.first_name + " " + self.last_name +".")
        print("login attempts: " + str(self.login_attempts) + '.')

    def greet_user(self):
        print("\nhello " + self.first_name + " " + self.last_name + ".")

class Admin(User):
    def __init__(self,first_name, last_name, login_attempts):
         super().__init__(first_name,last_name,login_attempts)
         self.privileges = 'can ban user'
    def show_privileges(self):
        print(self.privileges) 
 

class Car():
    """ 汽车基类"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) +
        " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("Now you've get your tank filed!")

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -KWh battery.")
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "  + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("There is no tank in electric car!")


from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'pyhton'

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is: " +
        language.title() + ".")

from collections import OrderedDict
vocabulary = OrderedDict()
vocabulary['p'] = 'python'
vocabulary['b'] = 'bash'
vocabulary['c'] = 'cpp'
vocabulary['s'] = 'shell'

for s, word in vocabulary.items():
    message = "start with " + s + " : " + word
    print(message)

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = 6
    def roll_die(self):
        return randint(1, self.sides)

d = Die(30)
t = 0
while t < 10:
    print(str(d.roll_die()))
    t += 1

from survey import AnonymousSurvey
import unittest

class TestAnonmyousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

unittest.main()

'''
import unittest
class Employee():
    def __init__(self, first, last, income):
        self.first = first
        self.last = last
        self.income = income
    
    def give_raise(self, increment=5000):
        self.income += increment
    

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('fan', 'mingrui', 5000)
    def test_give_default_raise(self):
        self.employee.give_raise() 
        self.assertEqual(self.employee.income, 10000)
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.income, 15000)
unittest.main()
