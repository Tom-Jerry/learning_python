#-*- coding: utf-8 -*-
def city_of_country(city, country,population=0):
    if population == 0:
        result = city + ',' +country
    else:
        result = city + ',' + country + ',' + str(population)
    return result