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

centrPoziom = [1, 1, 1]
centrPion = [0, 0, 0]
centrCyl = [-1, -1, -1]

promienCylindra = 1
krokAlfa = 1 #kąt kroku w stopniach
iloscKrokowAlfa = int(360/krokAlfa)
print(iloscKrokowAlfa)
for j in range(0, iloscKrokowX - 1):
    for i in range(0, iloscKrokowY - 1):
        punktyPoziomejPowierzchni.append([j * krokX + centrPoziom[0], i * krokY + centrPoziom[1], 0 + centrPoziom[2]])
        punktyPoziomejPowierzchni.append([-j * krokX + centrPoziom[0], -i * krokY + centrPoziom[1], 0 + centrPoziom[2]])
        punktyPoziomejPowierzchni.append([j * krokX + centrPoziom[0], -i * krokY + centrPoziom[1], 0 + centrPoziom[2]])
        punktyPoziomejPowierzchni.append([-j * krokX + centrPoziom[0], i * krokY + centrPoziom[1], 0 + centrPoziom[2]])

for j in range(0, iloscKrokowX - 1):
    for i in range(0, iloscKrokowZ - 1):
        punktyPionowejPowierzchni.append([j * krokX + centrPion[0], centrPion[1], i * krokZ + centrPion[2]])
        punktyPionowejPowierzchni.append([-j * krokX + centrPion[0], centrPion[1], -i * krokZ + centrPion[2]])
        punktyPionowejPowierzchni.append([j * krokX + centrPion[0], centrPion[1], -i * krokZ + centrPion[2]])
        punktyPionowejPowierzchni.append([-j * krokX + centrPion[0], centrPion[1], i * krokZ + centrPion[2]])

for i in range(0, iloscKrokowAlfa):
    for j in range(0, iloscKrokowZ):
        punktyCylindrycznejPowierzchni.append([promienCylindra * math.cos(math.radians(i * krokAlfa)) + centrCyl[0], promienCylindra * math.sin(math.radians(i * krokAlfa)) + centrCyl[1], j * krokZ + centrCyl[2]])
        punktyCylindrycznejPowierzchni.append([promienCylindra * math.cos(math.radians(i * krokAlfa)) + centrCyl[0], promienCylindra * math.sin(math.radians(i * krokAlfa)) + centrCyl[1], -j * krokZ + centrCyl[2]])

sciezka = "C:\\Users\\ara22\\Desktop\\point.xyz"

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
