import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans


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

plt.figure()

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