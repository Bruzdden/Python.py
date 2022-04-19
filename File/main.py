
class Halo:
  def __init__(self):
      self.rok = 0
  def Roky(self):
    self.rok = int(input("rok: "))
    print(self.rok) 
    if self.rok % 400 == 0:
        print("\nrok je přestupný")
    elif self.rok % 100 == 0:
        print("\nnení přestupný rok")   
    elif self.rok % 4 ==0:
        print("\nrok je přestupný")
    else:
        print("\nnení přestupný rok") 
class VypocetObjemu:
    def __init__(self):
        self.a, self.b, self.c = 0,0,0
    def VypocetKrychle(self):
        self.a = int(input("napis stranu a: "))
        if self.a == 0:
            print("0 nejde")
        else:
            self.celek = (self.a * self.a * self.a)
            self.celeks = (6 * self.a * self.a)
            print("Objem Krychle: ",self.celek, "povch:", self.celeks)
            print("Vzorec pro výpořet objemu: a*a*a")
            print("Vzorec pro výpočet povrchu: 6*a*a")
    def VypocetKvadru(self):
        self.a = int(input("napis stranu a: "))
        self.b = int(input("napis stranu b: "))
        self.c = int(input("napis stranu c: "))
        if self.a == 0 or self.b == 0 or self.c == 0:
          print("0 nejde")
        else:
          self.celek = (self.a * self.b * self.c)
          self.celeks = 2*(self.a*self.b + self.a*self.c + self.b*self.c)
          print("Objem Kvadru: ",self.celek, "povch:", self.celeks)
          print("Vzorec pro výpořet objemu: a*b*c")
          print("Vzorec pro výpočet povrchu: 2(ab + ac + bc)")
    def VypocetKoule(self):
        self.pi = 3.14
        self.r = float(input("napis r (polomer koule): "))
        if self.r == 0:
            print("0 nejde")
        else:
            self.celek = (4/3)*(self.pi*(self.r*self.r*self.r))
            self.celeks = (4)*(self.pi*(self.r*self.r))
            print("Objem Koule: ",self.celek, "povch:", self.celeks)
            print("Vzorec pro výpořet objemu: 4/3(pi*(r*r*r*))")
            print("Vzorec pro výpočet povrchu: 4(pi(r*r))")
