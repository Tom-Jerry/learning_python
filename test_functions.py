#-*- coding: utf-8 -*-
import unittest 
from city_funcitons import city_of_country

class CityCountryTest(unittest.TestCase):
    def test_city_country(self):
        city_country = city_of_country('Bristol', 'England')
        self.assertEqual(city_country, 'Bristol,England')
    
unittest.main()