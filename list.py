import random
mapa = list(range(0,10))
cislo = random.choice(mapa)
pocet_pokusu = 0
print("vyber číslo od 1 do 9")
while pocet_pokusu < 3:
    hadej = int(input())
    print("vybral si: ", hadej)
    print("mapa je:", *mapa)
    pocet_pokusu += 1
    if hadej != cislo:
        print("netrefil ses, zkus znovu")
    if hadej == cislo:
        print ("vyhral si, dalo ti to ", str(pocet_pokusu),  " pokus")
        mapa[hadej] = "*"
        break
        
        
        
        
        
        
        
        
        
        
        #27
