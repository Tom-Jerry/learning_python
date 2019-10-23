# -*- coding: utf-8 -*-

class Dog():
    def __init__(self, name, age):
        """ 初始化类的各个属性"""
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over.")

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

u = User('fan', 'mingrui', 0)
u.describe_user()
u.increment_login_attempts()
u.increment_login_attempts()
u.increment_login_attempts()
u.describe_user()
u.reset_login_attempts()
u.describe_user()