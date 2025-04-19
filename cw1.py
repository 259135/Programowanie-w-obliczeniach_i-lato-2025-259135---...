import math

punktyPoziomejPowierzchni=[]
punktyPionowejPowierzchni=[]
punktyCylindrycznejPowierzchni=[]

iloscKrokowX = 100
iloscKrokowY = 100
iloscKrokowZ = 100

krokX = 0.01
krokY = 0.01
krokZ = 0.01

promienCylindra = 1
krokAlfa = 1 #kąt kroku w stopniach
iloscKrokowAlfa = int(360/krokAlfa)
print(iloscKrokowAlfa)
for j in range(0, iloscKrokowX - 1):
    for i in range(0, iloscKrokowY - 1):
        punktyPoziomejPowierzchni.append([j * krokX, i * krokY, 0])
        punktyPoziomejPowierzchni.append([-j * krokX, -i * krokY, 0])
        punktyPoziomejPowierzchni.append([j * krokX, -i * krokY, 0])
        punktyPoziomejPowierzchni.append([-j * krokX, i * krokY, 0])

for j in range(0, iloscKrokowX - 1):
    for i in range(0, iloscKrokowZ - 1):
        punktyPionowejPowierzchni.append([j * krokX, 0, i * krokZ])
        punktyPionowejPowierzchni.append([-j * krokX, 0, -i * krokZ])
        punktyPionowejPowierzchni.append([j * krokX, 0, -i * krokZ])
        punktyPionowejPowierzchni.append([-j * krokX, 0, i * krokZ])

for i in range(0, iloscKrokowAlfa):
    for j in range(0, iloscKrokowZ - 1):
        punktyCylindrycznejPowierzchni.append([promienCylindra * math.cos(math.radians(i * krokAlfa)), promienCylindra * math.sin(math.radians(i * krokAlfa)), j * krokZ])
        punktyCylindrycznejPowierzchni.append([promienCylindra * math.cos(math.radians(i * krokAlfa)), promienCylindra * math.sin(math.radians(i * krokAlfa)), -j * krokZ])

#print(punktyPoziomejPowierzchni)
sciezka = "C:\\Users\\ara22\\Desktop\\point.xyz"
sciezka2 = "C:\\Users\\ara22\\Desktop\\point2.xyz"
sciezka3 = "C:\\Users\\ara22\\Desktop\\point3.xyz"

plik = open(sciezka, "w")
for i in punktyPoziomejPowierzchni: #dodawaj poszczególne elementy listy do pliku
    plik.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik.close()

plik2 = open(sciezka2, "w")
for i in punktyPionowejPowierzchni: #dodawaj poszczególne elementy listy do pliku
    plik2.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik2.close()

plik3 = open(sciezka3, "w")
for i in punktyCylindrycznejPowierzchni: #dodawaj poszczególne elementy listy do pliku
    plik3.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik3.close()
