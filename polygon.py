class Polygon:
    def __init__(self):
        pass
    def sett(self):
        pass
    def numOfSides(self):
        pass
class Triangle(Polygon):
    def __init__(self, **kwargs):
        self.__PocetStran = int(kwargs["pocet"]) if "pocet" in kwargs.keys() else 0
        self.__cislo = 0
    def sett(self, strr = None):
        self.__PocetStran = strr
    def numOfSides(self):
        return self.__PocetStran
class Pentagon(Polygon):
    def __init__(self, **kwargs):
        self.__PocetStran = int(kwargs["pocet"]) if "pocet" in kwargs.keys() else 0
        self.__cislo = 0
    def sett(self, strr = None):
        self.__PocetStran = strr
    def numOfSides(self):
        return self.__PocetStran
class Oktagon(Polygon):
    def __init__(self, **kwargs):
        self.__PocetStran = int(kwargs["pocet"]) if "pocet" in kwargs.keys() else 0
        self.__cislo = 0
    def sett(self, strr = None):
        self.__PocetStran = strr
    def numOfSides(self):
        return self.__PocetStran

#Instance
triangle = Triangle()
pentagon = Pentagon()
oktagon = Oktagon()

triangle.sett(3)
pentagon.sett(5)
oktagon.sett(8)

print(triangle.numOfSides())
print(pentagon.numOfSides())
print(oktagon.numOfSides())

