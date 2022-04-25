class Vehicle:
    def __init__(self, zvuk, kolo):
        self.zvuk = zvuk
        self.kolo = kolo
    def __str__(self):
        return f"Vozidlo ma zvuk {self.zvuk} a ma {self.kolo} kola"
class Car(Vehicle):
    def __init__(self,zvuk, kolo):
        super().__init__(zvuk, kolo)
        
    def __str__(self):
        return f"Vozidlo je {type(self).__name__} a ma zvuk {self.zvuk} a ma {self.kolo} kola"
    def startuje(self,znacka):
        self.znacka = znacka
        print(f"Auto startuje a ma znacku {self.znacka}")
class Motorbike(Vehicle):
    def __init__(self,zvuk, kolo):
        super().__init__(zvuk, kolo)
    def stoji(self, znacka):
        self.znacka = znacka
        print(f"Motorka stoji a ma znacku {self.znacka}")
    def __str__(self):
        return f"Vozidlo je {type(self).__name__} a ma zvuk {self.zvuk} a ma {self.kolo} kola"
class Truck(Vehicle):
    def __init__(self,zvuk, kolo):
        super().__init__(zvuk, kolo)
    def nemaparu(self, znacka):
        self.znacka = znacka
        print(f"Truck nemaparu a ma znacku {self.znacka}")
    def __str__(self):
        return f"Vozidlo je {type(self).__name__} a ma zvuk {self.zvuk} a ma {self.kolo} kola"

vehicle = Vehicle("vrrr", 0)
auto = Car("vrrr",4)
auto.startuje("subaru")
motorka = Motorbike("vr", 2)
motorka.stoji("Honda")
truck = Truck("vrrrrrrr",4)
truck.nemaparu("Jeep")
print(vehicle); print(auto); print(motorka); print(truck)
