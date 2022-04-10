import ipaddress
from appJar import gui

sit = input("napis sit:")
IPadresa = ipaddress.IPv4Network(sit)
maska = print("Maska adresy:", IPadresa.netmask)
network= print("Network adresy:", IPadresa.network_address)
broadcast=print("Broadcast adresy:", IPadresa.broadcast_address)
adres = IPadresa.num_addresses
adresy =print("Počet adres:", adres)
hosti = print("Počet hostů:", adres-2)
 
def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()
app = gui()
app.setSticky("news")
fileMenu = ["Quit"]
app.addMenuList("Adresy", fileMenu, onMenuItemSelect)
tabulka = [["",""],
  ["Maska adresy", IPadresa.netmask],
             ["Network adresy", IPadresa.network_address],
             ["Broadcast adresy", IPadresa.broadcast_address],
             ["Počet adres", adres],
           ["Počet hostů", adres-2]]
app.addGrid("grid", tabulka)
 
app.go()
