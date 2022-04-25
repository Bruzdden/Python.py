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
    def stoji(self, znacka, vlastnik):
        self.znacka = znacka
        self.vlastnik = vlastnik
        print(f"Motorka stoji a ma znacku {self.znacka} a vlastní ji {self.vlastnik}")
    def __str__(self):
        return f"Vozidlo je {type(self).__name__} a ma zvuk {self.zvuk} a ma {self.kolo} kola"
class Truck(Vehicle):
    def __init__(self,zvuk, kolo, rok):
        super().__init__(zvuk, kolo)
        self.rok = rok
    def nemaparu(self, znacka):
        self.znacka = znacka
        print(f"Truck nemaparu a ma znacku {self.znacka}")
    def __str__(self):
        return f"Vozidlo je {type(self).__name__} a ma zvuk {self.zvuk} a ma {self.kolo} kola, je z roku {self.rok}"

zvuk = str(input("napis zvuk auta:"))
zvukm = str(input("napis zvuk motorky:"))
zvukt = str(input("napis zvuk trucku:"))
vehicle = Vehicle("vrrr", "nekolik")
auto = Car(zvuk,4)
auto.startuje("Subaru")
motorka = Motorbike(zvukm, 2)
motorka.stoji("Honda","Patrik")
truck = Truck(zvukt,4,2001)
truck.nemaparu("Jeep")
print(vehicle); print(auto); print(motorka); print(truck)
