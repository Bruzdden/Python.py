hlavy = int(input())
nohy = int(input())
print("Počet hlav:", hlavy,"\nPočet noh:", nohy)
p = hlavy + nohy
print("Počet hlav a nohou dohromady:", p)
slepice = (nohy - (2 * hlavy)) // 2
kravy = (nohy - (4 * slepice)) // 2
PN = (slepice * 2) + (kravy * 4)
if not PN == nohy:
    print("\nnení možné, zadejte jiné čísla")
else:
    print("Počet noh slepic je", slepice * 2, "\nPočet noh krav je", kravy * 4)
    if slepice < 0 or kravy < 0:
        print("\nnení možné, zadejte jiné čísla")
    else:
        print("Slepice:", slepice, "\nKravy:", kravy)










#27
