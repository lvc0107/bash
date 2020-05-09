def is_casi_palindromo(a):
    n = len(a)
    mitad_1 = a[:n // 2]
    if n % 2 == 0:
        mitad_2 = a[n // 2:]
    else:
        mitad_2 = a[n // 2 + 1:]
    pass

    x = mitad_1
    y = ''.join(reversed(mitad_2))
    if x == y:
        return True
    else:
        count_diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count_diff += 1

        return count_diff == 1


print(is_casi_palindromo("abccba"))
print(is_casi_palindromo("abccbx"))
print(is_casi_palindromo("abccfg"))


class A(object):
    bro = []

    def __init__(self, name, *args):
        self.name = name


a = A('Richar')
b = A('Ellie')

a.bro.append('jhon')

print(a.name, a.bro, b.name, b.bro)

a = [1, 2, 3]
b = a
a = [1, 2, 4]
print(b)

from datetime import datetime


class Human(object):
    name = None
    birthday = None

    def __init__(self, name=None):
        if name == 'age':
            return datetime.now() - self.birthday
        else:
            return None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)


h = Human()
h.birthday = datetime(1984, 8, 20)
h.age = 28
print(h.age)

import copy
class A(object):
    pass


a = A()
a.lst = [1, 2, 3]
a.str = "cats and dogs"
b = copy.copy(a)
c = copy._copy_immutable(a)
a.lst.append(100)
a.str = "cats and mice"
print(b.lst)
print(b.str)
print(c.lst)
print(c.str)


import random


def func(type_='s'):
    if type_ == 's':
        return 'Mark'
    elif type_ == 'i':
        return random.randint(0, 1000)


def dec(func, type_):
    x = 8

    def wrape():
        value = func(type_)
        if isinstance(value, int):
            return value * x

    return wrape

print(dec(func, 'i')())


class A(object):
    def __repr__(self):
        return 'instance A'


a = A()
b = a
del a
print(b)
print(a)
