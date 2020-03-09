import math as mh
import datetime


def arithmetic(a, b, operator):
    if operator is '+':
        result = a + b
    elif operator is '-':
        result = a - b
    elif operator is '*':
        result = a * b
    elif operator is '/':
        result = a / b
    else:
        result = 'unknown operator'
    return result


print('result =', arithmetic(5, 10, 'v'))
print('result =', arithmetic(5, 10, '+'))


def is_year_leap(year):
    if not (year % 400):
        return True
    elif not (year % 100):
        return False
    elif not (year % 4):
        return True
    else:
        return False


print(is_year_leap(2016))
print(is_year_leap(2015))

def square(side):
    return (side * 4, side * side, side * mh.sqrt(2))


print(square(2))


def seasons(month):
    if month > 12:
        return 'invalid number'
    elif month in (1, 2, 12):
        return 'winter'
    elif month in range(3, 6):
        return 'spring'
    elif month in range(6,9):
        return 'summer'
    elif month in range(9, 12):
        return 'autumn'


print(seasons(12))


def bank(a, years):
    for i in range(years):
        a = a + a * 0.1
    return a


print(bank(100000, 100))


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(mh.sqrt(a)) + 1):
        if not (a % i):
            return False
    return True


print(is_prime(199))


def date_cheat(day, month, year):
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True


print(date_cheat(29, 2, 2016))


def XOR_cipher(str, key):
    result = []
    for i in range(len(str)):
        result.append(chr(ord(str[i]) ^ ord(key[i % len(key)])))
    return result


XOR_uncipher = XOR_cipher


temp = XOR_cipher('spagetti', 'sauce')
print(temp)
print(XOR_uncipher(temp, 'sauce'))
