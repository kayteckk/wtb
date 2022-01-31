#
# print("1. dodawanie")
# print("2. odejmowanie")
# print("4. wylacz")
# x = input()
# print("podaj pierwsza liczbe: ")
# l1 = input()
# print("podaj druga liczbe: ")
# l2 = input()

def dzialanie(x,l1,l2):
    if x == 1:
        dodawanie(l1,l2)
    if x == 2:
        odejmowanie(l1,l2)
    if x == 4:
        return 0

def dodawanie(l1,l2):
    wynikowa = l1+l2
    print(wynikowa)
    return wynikowa

def odejmowanie(l1,l2):
    wynikowa = l1-l2
    print(wynikowa)
    return wynikowa