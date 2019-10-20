#-*- coding: utf-8 -*-
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
'''
print area
print("you ordered a " + pizza['crust'] + "-crust pizza"
    + "with the following toppings: " )

for topping in pizza['toppings']:
    print("\t" + topping)

'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name + "'s favorite languages are:")
        for l in languages:
            print("\t" + l.title())
    else:
        print('\n', name, '\'s favorite language is', languages)