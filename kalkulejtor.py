#
# print("1. dodawanie")
# print("2. odejmowanie")
# print("4. wylacz")
# x = input()
# print("podaj pierwsza liczbe: ")
# l1 = input()
# print("podaj druga liczbe: ")
# l2 = input()
import math as m
def dodawanie(l1,l2):
    wynikowa = l1+l2
    print(wynikowa)
    return wynikowa

def odejmowanie(l1,l2):
    wynikowa = l1-l2
    print(wynikowa)
    return wynikowa

def mnozenie(l1,l2):
    wynikowa=l1*l2
    print(wynikowa)
    return wynikowa

def dzielenie(l1,l2):
    wynikowa = l1/l2
    print(wynikowa)
    return wynikowa
def pierwiastek(l1):
    wynikowa = m.sqrt(l1)
    print(wynikowa)
    return wynikowa
def potega(l1,stopien):
    wynikowa = m.pow(l1,stopien)
    print(wynikowa)
    return wynikowa