class Polygon:
    def __init__(self):
        pass
    def set(self):
        pass
    def get(self):
        pass
        def numOfSides(self):
            pass
class Triangle(Polygon):
    def __init__(self, **kwargs):
        self.__PocetStran = int(kwargs["pocet"]) if "pocet" in kwargs.keys() else 0
        self.__cislo = 0
class Pentagon(Polygon):
    def __init__(self, **kwargs):
        self.__PocetStran = int(kwargs["pocet"]) if "pocet" in kwargs.keys() else 0
        self.__cislo = 0
class Oktagon(Polygon):
    def __init__(self, **kwargs):
        self.__PocetStran = int(kwargs["pocet"]) if "pocet" in kwargs.keys() else 0
        self.__cislo = 0
