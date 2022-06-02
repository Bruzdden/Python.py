from math import *
class Usecka:
    def __init__(self):
        self.lat1 = radians(50.99431103661443)
        self.long1 = radians(14.56902810489412)
        self.lat2 = radians(50.563354506789466)
        self.long2 = radians(14.654259111192149)
    def pocet(self):
        a = sin((self.lat2 - self.lat1)/2)**2 + cos(self.lat1) * cos(self.lat2) * sin((self.long2 -self.long1)/2)**2
        c = 2 * atan2( sqrt(a), sqrt(1-a) )
        #e = acos[sin(self.lat1) * sin(self.lat2) + cos(self.lat1) * cos(self.lat2) * cos(self.long1 - self.long2)] * 6371.0
        d = 6371.0 * c
        print(d)
U = Usecka(); U.pocet()
