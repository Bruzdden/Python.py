class Hero:
    def __init__(self, name = "", born = 0, weapons = [], bestActorname = ""):
        self.__name = name
        self.__born = born
        self.__weapons = weapons
        self.__bestAN = bestActorname
    def setName(self, name = ""):
        self.__name = name
    def setBorn(self, born = 0):
        self.__born = born
    def setBestActorName(self, StrBestAN = ""):
        self.__bestAN = StrBestAN
    def getName(self):
        return self.__name
    def getBorn(self):
        return self.__born
    def getBestActorName(self):
        return self.__bestAN
    def addWeapon(self, weapon):
        self.__weapons = weapon
    def removeWeapon(self):
        del self.__weapons
    def getWeapons(self):
        return self.__weapons

hero = Hero()
print(hero)
hero.setName("Chris")
hero.setBorn(1981)
hero.setBestActorName("Robert")
hero.addWeapon("oblek")
print("Jmeno: {}".format(hero.getName()))
print("Narození: {}".format(hero.getBorn()))
print("Nejlepší herec: {}".format(hero.getBestActorName()))
print("Zbraně: {}".format(hero.getWeapons()))
print(f"nejlepší herec", hero.getBestActorName())
