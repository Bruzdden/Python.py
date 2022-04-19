from main import *
halo= Halo()
vypocet = VypocetObjemu()

print("Program")
program = str(input("Vyber si Program, pro spusteni programu na vypocet prestupnyho roku napis (roky) bez závorky, pro spusteni programu na vypocet objemu kvadru (kvadr), pro vypocet krychle (krychle) a pro vypocet koule (koule):"))
if program == "roky":
    halo.Roky()
elif program == "kvadr":
    vypocet.VypocetKvadru()
elif program == "krychle":
    vypocet.VypocetKrychle()
elif program == "koule":
    vypocet.VypocetKoule()
else: print("Tento program neexistuje :(")
