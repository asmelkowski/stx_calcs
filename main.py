import math

# Wykorzystując paradygmaty programowania obiektowego napisz program który będzie pozwalał na obliczanie pół i objętości figur płaskich oraz wielościanów.
# * trójkąt
# * kwadrat
# * prostokąt
# * sześcian
# * ostrosłup foremny
# * owal

class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def calc_surface(self):
        return 0.5 * self.a * self.h


class Square:
    def __init__(self, a):
        self.a = a

    def calc_surface(self):
        return self.a**2


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a * self.b


class Cube:
    def __init__(self, a):
        self.a = a

    def calc_surface(self):
        return 6*self.a**2
    
    def calc_volume(self):
        return self.a**3


class Tetrahedron:
    def __init__(self, a):
        self.a = a

    def calc_surface(self):
        return self.a**2 * math.sqrt(3)
    
    def calc_volume(self):
        return (self.a**3 * math.sqrt(2))/12


class Oval:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return math.pi*self.a*self.b



