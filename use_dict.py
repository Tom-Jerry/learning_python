# -*- coding: utf-8 -*-
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

'''
# test area
for name, language in favorite_languages.items():
    print('\nname:',name, '\nlanguage:', language)

for k,v in user_0.items():
    print("\nkey:" + k)
    print("value:" + v)

for name in favorite_languages.keys():
    print(name.title())

index_name = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in index_name:
        print('Hi', name.title(), 'I know your favorite language is',
        favorite_languages[name].title(), '!')
    print()

    for name in sorted(favorite_languages.keys()):
    print(name.title() + "'s favorite language is" +" " + favorite_languages[name])

print("The following language are mentioned:")
for lan in set(favorite_languages.values()):
    print(lan.title())

'''


top_3_rivers = {
    'nile':'egypt',
    'yangtz':'china',
}

for river_name in top_3_rivers.keys():
    print(river_name)
for nation_name in top_3_rivers.values():
    print(nation_name)

candidates = ['jen', 'sarah', 'edward', 'phil', 'lebron', 'harden']
for p in candidates:
    if p in favorite_languages.keys():
        print("Thanks for attending the query " + p)
    else:
        print("Please join our query " + p)