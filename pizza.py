# -*-coding:utf-8 -*-
def make_pizza(size, *toppings):
    """ 概述將要制作的批薩"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print(" - " + topping)
