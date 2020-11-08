from large_population_find import one_word
import unittest

class CitiesTestCase(unittest.TestCase):
    def test_large_population(self):
        city_population =large_population(3000)
                            #Is the city one word? If so, return True. If not, fals
        self.assertAlmostEqual(city_population, '2000')

unittest.main()
