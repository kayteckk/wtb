from kalkulejtor import *
import unittest
class CalculatorTests(unittest.TestCase):
    def test_dodawanie(self):
        l1 = 5
        l2 = 6
        assert dodawanie(l1,l2) == 11
    def test_odejmowanie(self):
        l1=-8
        l2=3
        assert odejmowanie(l1,l2) == -11
    def test_mnozenie(self):
        l1=8.5
        l2=30
        assert mnozenie(l1,l2) == 255
    def test_dzielenie(self):
        l1=9
        l2=2
        assert dzielenie(l1,l2) == 4.5
    def test_pierwiastek(self):
        l1=16
        assert pierwiastek(l1) == 4
    def test_potega(self):
        l1=8
        stopien=3
        assert potega(l1,stopien) == 512

if __name__ == '__main__':
    unittest.main()