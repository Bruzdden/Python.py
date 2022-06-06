""" Dědičnost
    Usecka používá jako vstupní parametry konstruktoru __init__ instance třídy Bod.
    Instance třídy Bod jsou vytvořeny mimo instanci třídy Usecka.
    Hodnoty souřadnic jsou předávány v podobě slovníku, např. {"x": 1, "y": 3}.

"""

import os
import math

clear = lambda: os.system('cls')

class Bod:
    
    def __init__(self, B: dict):
        self.souradnice = B

    def nastavSouradnice(self, x, y):
        self.souradnice["x"] = x
        self.souradnice["y"] = y

    def getx(self):
        return self.__x
    def setx(self, x = 0):
        self.__x = x
    def gety(self):
        return self.__y
    def sety(self, y = 0):
        self.__y = y

    def __str__(self):
        return "[{},{}]".format(self.souradnice["x"], self.souradnice["y"])
    
class Usecka:

    def __init__(self, A: Bod, B: Bod):
        self.__a = A
        self.__b = B
    
    def nastavSouradnice(self, A: dict, B: dict):
        self.__a.nastavSouradnice(A["x"], A["y"])
        self.__b.nastavSouradnice(B["x"], B["y"])

    def getA(self):
        return self.__a
    def setA(self, value):
        self.__a = value
    def getB(self):
        return self.__b
    def setB(self, value):
        self.__b = value

    def __str__(self):
        return  "[{},{}][{},{}]".format(self.__a.souradnice["x"], self.__a.souradnice["y"], self.__b.souradnice["x"], self.__b.souradnice["y"])

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.__a.souradnice["x"] - self.__b.souradnice["x"], 2) + math.pow(self.__a.souradnice["y"] - self.__b.souradnice["y"], 2))
    
clear()

B = Bod({"x": 1, "y": -2})
print(B)

D = Bod({"x": 1, "y": 3})
E = Bod({"x": 4, "y": -1})
U = Usecka(D, E)

print(U)
print(f"{U.delkaUsecky():.2f}")
