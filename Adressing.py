import ipaddress

sit = input("napis sit:")
IPadresa = ipaddress.IPv4Network(sit)
print("Maska adresy:", IPadresa.netmask)
print("Network adresy:", IPadresa.network_address)
print("Broadcast adresy:", IPadresa.broadcast_address)
