import math
from math import pi
from random import random, randint
import random


def test_hello():
    name = "Анна"
    age = 25
    a = "Привет"
    b = "Тебе"
    c = "лет"
    output = f"{a}, {name}! {b} {age} {c}."
    print(output)
    assert output == "Привет, Анна! Тебе 25 лет."

def test_rectangle():

    a = 10
    b = 20

# TODO сосчитайте периметр
    perimeter = (a+b)*2
    assert perimeter == 60
# TODO сосчитайте площадь
    area = a*b
    assert area == 200

def test_circle():
    r = 23
# TODO сосчитайте площадь
    area = pi*r**2
    print(area)
    assert area == 1661.9025137490005
# TODO сосчитайте длину окружности
    length = 2*pi*r
    assert length == 144.51326206513048

def test_random_list():
# TODO создайте список
    l = random.sample(range(1,101),10)
    l.sort()
    print(l)
    assert len(l) == 10
    assert l[0] < l[-1]

def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
# TODO удалите повторяющиеся элементы
    l = list(set(l))
    print(l)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
# TODO создайте словарь
    d = dict(zip(first, second))
    print(d)
    assert isinstance(d, dict)
    assert len(d) == 5