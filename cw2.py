import csv
import math
import numpy as np
import pyransac3d
from numpy.random import default_rng
rng = default_rng()

from sklearn.cluster import KMeans

def ransac(dane, k, t, d):
    iteracja=0
    najlepsze_dopasowanie = null
    najlepszy_blad = +inf
    while iteracja<k :
        wp = rng.permutation(dane)[0:2] #Wybrane Punkty
        a = [wp[1][0] - wp[0][0], wp[1][1] - wp[0][1], wp[1][2] - wp[0][2]]
        b = [wp[2][0] - wp[0][0], wp[2][1] - wp[0][1], wp[2][2] - wp[0][2]]

        A = a[1] * b[2] - a[2] * b[1]
        B = -(a[0] * b[2] - a[2] * b[0])
        C = a[0] * b[1] - a[1] * b[0]
        D = -A * wp[0][0] - B * wp[0][1] - C * wp[0][2]
        axb = [A, B, C]

        zaakceptowane_bliskie = []
        for l in dane:
            d = abs(A * l[0] + B * l[1] + C * l[2] + D)/math.sqrt(pow(A, 2) + pow(B, 2) + pow(C, 2))
            if d < t:
                zaakceptowane_bliskie.append(l)
        if len(zaakceptowane_bliskie) > d:
            


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

clusterer = KMeans(n_clusters=3)
pArray = np.array(punkty)
y = clusterer.fit_predict(pArray)

klaster1 = y == 0
klaster2 = y == 1
klaster3 = y == 2

k1Punkty = pArray[klaster1]
k2Punkty = pArray[klaster2]
k3Punkty = pArray[klaster3]

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


