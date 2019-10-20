#-*- coding:utf-8 -*-
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

#aliens = [alien_0, alien_1, alien_2]
#for it in aliens:
    #print(it)

aliens = []
for alien_number in range(30):
    new_alien = {
        'color':'default',
        'points':'default',
        'speed':'default',
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'default':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    
for alien in aliens[:5]:
    print(alien)
print('......')

print("total number of aliens： " + str(len(aliens)))