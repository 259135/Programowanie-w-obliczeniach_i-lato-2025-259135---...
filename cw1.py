print("Test")
punktyPoziomejPowierzchni=[]
iloscKrokow = 10
krokX = 0.1
krokY = 0.1

for j in range(0, iloscKrokow):
    for i in range(0, iloscKrokow):
        punktyPoziomejPowierzchni.append([j * krokX, i * krokY, 0])
        punktyPoziomejPowierzchni.append([-j * krokX, -i * krokY, 0])
        punktyPoziomejPowierzchni.append([j * krokX, -i * krokY, 0])
        punktyPoziomejPowierzchni.append([-j * krokX, i * krokY, 0])

print(punktyPoziomejPowierzchni)
sciezka = "C:\\Users\\ara22\\Desktop\\point.xyz"

plik = open(sciezka, "w")
for i in punktyPoziomejPowierzchni: #dodawaj poszczególne elementy listy do pliku
    plik.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik.close()