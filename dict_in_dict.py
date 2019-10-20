# -*- coding: utf-8 -*-
users = {
    'FanMingrui':{
        'first':'Mingrui',
        'second':'Fan',
        'location':'BeiJing',
    },

    'HuangYiman':{
        'first':'Yiman',
        'second':'Fan',
        'location':'Chengdu',
    },
}

for user_name,user_info in users.items():
    print('\n\tUsername:', user_name)
    full_name = user_info['first'] + " " + user_info['second']
    location = user_info['location']

    print('\tFull name:', full_name.title())
    print('\tLocation:', location.title())