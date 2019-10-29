#-*- coding: utf-8 -*-
import unittest
def get_formatted_name(first, last, middle=''):
    """Generate a neatly full name!"""
    if middle:
        full_name = first + middle + last
    else:
        full_name = first + ' ' + last
    return full_name
'''
print("Enter 'q' to quit at any time")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name)
'''

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name("Janis", "Joplin")
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()