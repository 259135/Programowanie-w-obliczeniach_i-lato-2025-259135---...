import math
import csv
import numpy as np
import pyransac3d

print("Skrypt realizujący drugą część zadania 2. Autor: 259135")
print("Użycie algorytmu RANSAC do rzeczywistej chmury punktów (Conference Room) i podział jej na ściany.")
punkty = []
sciezka = input("Podaj ścieżkę do pliku chmury punktów (Conference Room)...")
with open(sciezka, newline='\n') as plik:
    csvPunkty = csv.reader(plik, delimiter=' ')
    for row in csvPunkty:
        #odczyt punktów do tablicy
        pt = []
        pt.append(float(row[0]))
        pt.append(float(row[1]))
        pt.append(float(row[2]))
        punkty.append(pt)

#konwersja do tablicy np
pArray = np.array(punkty)

sciezka = input("Podaj katalog wyjściowy. Ścieżkę zakończ ukośnikiem...")

#utworzenie obiektu klasy, która dopasowuje płaszczyznę do chmury punktów
ransac3d = pyransac3d.Plane()
for i in range(1,7):
    print(str(i) + ". iteracja")
    be,zb = ransac3d.fit(pArray,thresh=0.05, minPoints=180000, maxIteration=200) # max. odległość=0.05 (grubość ścian (uwzględniając ich nierównomierność) to max. 0.1), każda ze ścian to ok. 220000 punktów, stąd wartość nieco mniejsza: 180000; liczba iteracji=200.

    #zapis ściany do pliku
    plik1 = open(sciezka + "k" + str(i) + ".xyz", "w")
    for j in zb: #dodawaj poszczególne elementy listy do pliku
        plik1.write(str(pArray[j][0]) + " " + str(pArray[j][1]) + " " + str(pArray[j][2]) + "\n")
    plik1.close()

    pArray = np.delete(pArray,zb,axis=0) #usuwanie punktów określonych jako bliskie w danej iteracji, aby algorytm nie mógł wybierać wielokrotnie tych samych ścian.
    print("Współczynniki równania płaszczyzny: " + str(be))

print("Ściany zapisano w plikach " + sciezka + "k1.xyz do k6.xyz.")