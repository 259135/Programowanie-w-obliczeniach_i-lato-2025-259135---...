import math
from numpy.random import default_rng
rng = default_rng()

#tablice danych
punktyPoziomejPowierzchni=[]
punktyPionowejPowierzchni=[]
punktyCylindrycznejPowierzchni=[]

#ilość kroków w każdym wymiarze, jakie uczyni program przy generowaniu punktów
iloscKrokowX = 100
iloscKrokowY = 100
iloscKrokowZ = 100

#odległość pomiędzy punktami w każdym wymiarze
krokX = 0.01
krokY = 0.01
krokZ = 0.01

#punkty początkowe obiektów
centrPoziom = [1.2, 1.2, 1.2]
centrPion = [0, 0, 0]
centrCyl = [-1.2, -1.2, -1.2]

na = 0.03 #amplituda szumu (odchylenie standardowe)
promienCylindra = 1
krokAlfa = 1 #kąt kroku w stopniach
iloscKrokowAlfa = int(360/krokAlfa)

#Tworzenie płaszczyzny poziomej - kroki na X oraz Y, Z = 0. rng.normal(0,na) reprezentuje szum względem wyliczonej wartości współrzędnej
for j in range(0, iloscKrokowX - 1):
    for i in range(0, iloscKrokowY - 1):
        punktyPoziomejPowierzchni.append([j * krokX + centrPoziom[0] + rng.normal(0,na), i * krokY + centrPoziom[1] + rng.normal(0,na), 0 + centrPoziom[2] + rng.normal(0,na)])

#Tworzenie płaszczyzny pionowej - kroki na X oraz Z, Y = 0.
for j in range(0, iloscKrokowX - 1):
    for i in range(0, iloscKrokowZ - 1):
        punktyPionowejPowierzchni.append([j * krokX + centrPion[0] + rng.normal(0,na), centrPion[1] + rng.normal(0,na), i * krokZ + centrPion[2] + rng.normal(0,na)])

#Tworzenie cylindra. W płaszczyznie XY jest to złożenie sin i cos.
for i in range(0, iloscKrokowAlfa):
    for j in range(0, iloscKrokowZ):
        punktyCylindrycznejPowierzchni.append([promienCylindra * math.cos(math.radians(i * krokAlfa)) + centrCyl[0] + rng.normal(0,na), promienCylindra * math.sin(math.radians(i * krokAlfa)) + centrCyl[1] + rng.normal(0,na), j * krokZ + centrCyl[2] + rng.normal(0,na)])

#Zapis chmur punktów do pliku.
sciezka = input("Podaj ścieżkę do zapisu...")

#Suma wszystkich obiektów.
wszystkiePunkty = []
wszystkiePunkty.extend(punktyPoziomejPowierzchni)
wszystkiePunkty.extend(punktyPionowejPowierzchni)
wszystkiePunkty.extend(punktyCylindrycznejPowierzchni)

#Zapis w formacie ASCII, trzy kolumny: X Y Z.
plik = open(sciezka, "w")
for i in wszystkiePunkty: #dodawaj poszczególne elementy listy do pliku
    plik.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
plik.close()
