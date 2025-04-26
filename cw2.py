import csv
import math
import scipy
import numpy as np
import pyransac3d
from sklearn.cluster import KMeans
from numpy.random import default_rng

rng = default_rng()

def ransac(dane, k, t, d):
    iteracja=0
    najlepsze_dopasowanie = None
    najlepszy_blad = math.inf
    while iteracja<k :
        wp = rng.permutation(dane)[0:3] #Wybrane Punkty
        a = [wp[1][0] - wp[0][0], wp[1][1] - wp[0][1], wp[1][2] - wp[0][2]]
        b = [wp[2][0] - wp[0][0], wp[2][1] - wp[0][1], wp[2][2] - wp[0][2]]

        A = a[1] * b[2] - a[2] * b[1]
        B = -(a[0] * b[2] - a[2] * b[0])
        C = a[0] * b[1] - a[1] * b[0]
        D = -A * wp[0][0] - B * wp[0][1] - C * wp[0][2]
        axb = [A, B, C]

        zaakceptowane_bliskie = []
        odleglosci_punktow_zaakceptowanych = []
        for l in dane:
            dd = abs(A * l[0] + B * l[1] + C * l[2] + D)/math.sqrt(pow(A, 2) + pow(B, 2) + pow(C, 2))
            if dd < t:
                zaakceptowane_bliskie.append(l)
                odleglosci_punktow_zaakceptowanych.append(dd)
        if len(zaakceptowane_bliskie) > d:
            aktualne_dopasowanie = axb
            aktualny_blad = np.mean(odleglosci_punktow_zaakceptowanych)   #określanie błędu
            if aktualny_blad < najlepszy_blad:
                najlepszy_blad = aktualny_blad
                najlepsze_dopasowanie = aktualne_dopasowanie
        iteracja = iteracja + 1
    if najlepszy_blad == math.inf:
        czy_plaszczyzna = "nie"
    else:
        czy_plaszczyzna = "tak"

    if najlepsze_dopasowanie is not None:
        najlepsze_dopasowanie=najlepsze_dopasowanie / np.linalg.norm(najlepsze_dopasowanie)
    return najlepsze_dopasowanie, najlepszy_blad, czy_plaszczyzna

print("Ładowanie danych")
sciezka1 = "C:\\Users\\ara22\\Desktop\\point_cl1.xyz"
sciezka2 = "C:\\Users\\ara22\\Desktop\\point_cl2.xyz"
sciezka3 = "C:\\Users\\ara22\\Desktop\\point_cl3.xyz"

punkty = []

with open("C:\\Users\\ara22\\Desktop\\point.xyz", newline='\n') as plik:
    csvPunkty = csv.reader(plik, delimiter=' ')
    for row in csvPunkty:
        #print(float(row))
        pt = []
        pt.append(float(row[0]))
        pt.append(float(row[1]))
        pt.append(float(row[2]))
        punkty.append(pt)

print("Klasteryzacja danych")
clusterer = KMeans(n_clusters=3)#, init=[[-1.2,-1.2,-1.2],[0,0,0],[1.2,1.2,1.2]])
pArray = np.array(punkty)
y = clusterer.fit_predict(pArray)

klaster1 = y == 0
klaster2 = y == 1
klaster3 = y == 2

k1Punkty = pArray[klaster1]
k2Punkty = pArray[klaster2]
k3Punkty = pArray[klaster3]

print("Zapis danych klastrów")
plik1 = open(sciezka1, "w")
for i in range(0,len(k1Punkty)): #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(k1Punkty[i][0]) + " " + str(k1Punkty[i][1]) + " " + str(k1Punkty[i][2]) + "\n")
plik1.close()

plik2 = open(sciezka2, "w")
for i in range(0,len(k2Punkty)): #dodawaj poszczególne elementy listy do pliku
    plik2.write(str(k2Punkty[i][0]) + " " + str(k2Punkty[i][1]) + " " + str(k2Punkty[i][2]) + "\n")
plik2.close()

plik3 = open(sciezka3, "w")
for i in range(0,len(k3Punkty)): #dodawaj poszczególne elementy listy do pliku
    plik3.write(str(k3Punkty[i][0]) + " " + str(k3Punkty[i][1]) + " " + str(k3Punkty[i][2]) + "\n")
plik3.close()

print("Analiza klastrów\n")
print("Analiza 1. klastra...")
nd1,nb1,czy1 = ransac(k1Punkty,200,0.1,0.7*len(k1Punkty))

print("Klaster nr 1:")
print("Wektor normalny: " + str(nd1))
print("Czy to płaszczyzna: " + czy1)
if czy1 =="tak":
    print("Średnia odległość punktu od płaszczyzny: " + str(nb1))
    if abs(nd1[0])<0.1 and abs(nd1[1])<0.1 and abs(nd1[2])>0.9:
        print("Ta płaszczyzna jest pozioma.")
    elif abs(nd1[2])<0.1 and (bool(abs(nd1[1])>0.9) ^ bool(abs(nd1[0])>0.9)):
        print("Ta płaszczyzna jest pionowa.")

print("")

print("Analiza 2. klastra...")
nd2,nb2,czy2 = ransac(k2Punkty,200,0.1,0.7*len(k2Punkty))

print("Klaster nr 2:")
print("Wektor normalny: " + str(nd2))
print("Czy to płaszczyzna: " + czy2)
if czy2 =="tak":
    print("Średnia odległość punktu od płaszczyzny: " + str(nb2))
    if abs(nd2[0])<0.1 and abs(nd2[1])<0.1 and abs(nd2[2])>0.9:
        print("Ta płaszczyzna jest pozioma.")
    elif abs(nd2[2])<0.1 and (bool(abs(nd2[1])>0.9) ^ bool(abs(nd2[0])>0.9)):
        print("Ta płaszczyzna jest pionowa.")
print("")

print("Analiza 3. klastra...")
nd3,nb3,czy3 = ransac(k3Punkty,200,0.1,0.7*len(k3Punkty))
print("Klaster nr 3:")
print("Wektor normalny: " + str(nd3))
print("Czy to płaszczyzna: " + czy3)
if czy3 =="tak":
    print("Średnia odległość punktu od płaszczyzny: " + str(nb3))
    if abs(nd3[0])<0.1 and abs(nd3[1])<0.1 and abs(nd3[2])>0.9:
        print("Ta płaszczyzna jest pozioma.")
    elif abs(nd3[2])<0.1 and (bool(abs(nd3[1])>0.9) ^ bool(abs(nd3[0])>0.9)):
        print("Ta płaszczyzna jest pionowa.")

