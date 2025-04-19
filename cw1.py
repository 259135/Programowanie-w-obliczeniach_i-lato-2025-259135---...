punktyPoziomejPowierzchni=[]
punktyPionowejPowierzchni=[]
iloscKrokowX = 10
iloscKrokowY = 10
iloscKrokowZ = 10
krokX = 0.1
krokY = 0.1
krokZ = 0.1

for j in range(0, iloscKrokowX):
    for i in range(0, iloscKrokowY):
        punktyPoziomejPowierzchni.append([j * krokX, i * krokY, 0])
        punktyPoziomejPowierzchni.append([-j * krokX, -i * krokY, 0])
        punktyPoziomejPowierzchni.append([j * krokX, -i * krokY, 0])
        punktyPoziomejPowierzchni.append([-j * krokX, i * krokY, 0])

for j in range(0, iloscKrokowX):
    for i in range(0, iloscKrokowZ):
        punktyPionowejPowierzchni.append([j * krokX, 0, i * krokZ])
        punktyPionowejPowierzchni.append([-j * krokX, 0, -i * krokZ])
        punktyPionowejPowierzchni.append([j * krokX, 0, -i * krokZ])
        punktyPionowejPowierzchni.append([-j * krokX, 0, i * krokZ])

print(punktyPoziomejPowierzchni)
sciezka = "C:\\Users\\ara22\\Desktop\\point.xyz"
sciezka2 = "C:\\Users\\ara22\\Desktop\\point2.xyz"

plik = open(sciezka, "w")
for i in punktyPoziomejPowierzchni: #dodawaj poszczególne elementy listy do pliku
    plik.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik.close()

plik2 = open(sciezka2, "w")
for i in punktyPionowejPowierzchni: #dodawaj poszczególne elementy listy do pliku
    plik2.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik2.close()