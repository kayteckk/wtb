from kalkulejtor import *
import unittest
class CalculatorTests(unittest.TestCase):
    def test_dodawanie(self):
        l1 = 5
        l2 = 6
        wynikowa = dodawanie(l1,l2)
        self.assertEqual(wynikowa,11)
    def test_odejmowanie(self):
        l1=-8
        l2=3
        wynikowa = odejmowanie(l1,l2)
        self.assertEqual(wynikowa,-11)
    

if __name__ == '__main__':
    unittest.main()