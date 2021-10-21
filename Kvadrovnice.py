from math import sqrt

a = float(input("a = "))
print(a)
b = float(input("b = "))
print(b)
c = float(input("c = "))
print(c)

D = (b * b) - (4 * a * c)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("Dvě řešení: x1 = {:.2}, x2 = {:.2}".format(x1, x2))
if D < 0:
    print("nemá řešení")
if D == 0:
    print("jedno řešení: x = {:.2}".format((-b) / (2 * a)))

#AUTHOR Lukáš Divíšek






#mám rád číslo 27
