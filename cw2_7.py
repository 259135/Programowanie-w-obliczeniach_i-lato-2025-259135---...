import math
import numpy as np
import pyransac3d

punkty = []

with open("C:\\Users\\ara22\\Desktop\\conferenceRoom_1.txt", newline='\n') as plik:
    csvPunkty = csv.reader(plik, delimiter=' ')
    for row in csvPunkty:
        #print(float(row))
        pt = []
        pt.append(float(row[0]))
        pt.append(float(row[1]))
        pt.append(float(row[2]))
        punkty.append(pt)

pArray = np.array(punkty)

ransac3d = pyransac3d.Plane()
be1,zb1 = ransac3d.fit(pArray,thresh=0.08, minPoints=100000, maxIteration=200)

plik1 = open("C:\\Users\\ara22\\Desktop\\k1.xyz", "w")
for i in zb1: #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(pArray[i][0]) + " " + str(pArray[i][1]) + " " + str(pArray[i][2]) + "\n")
plik1.close()

pArray = np.delete(pArray,zb1,axis=0)
print("1")
print(str(be1))

be2,zb2 = ransac3d.fit(pArray,thresh=0.08, minPoints=100000, maxIteration=200)

plik1 = open("C:\\Users\\ara22\\Desktop\\k2.xyz", "w")
for i in zb2: #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(pArray[i][0]) + " " + str(pArray[i][1]) + " " + str(pArray[i][2]) + "\n")
plik1.close()

pArray = np.delete(pArray,zb2,axis=0)
print("2")
print(str(be2))

be3,zb3 = ransac3d.fit(pArray,thresh=0.08, minPoints=100000, maxIteration=200)

plik1 = open("C:\\Users\\ara22\\Desktop\\k3.xyz", "w")
for i in zb3: #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(pArray[i][0]) + " " + str(pArray[i][1]) + " " + str(pArray[i][2]) + "\n")
plik1.close()

pArray = np.delete(pArray,zb3,axis=0)
print("3")
print(str(be3))

be4,zb4 = ransac3d.fit(pArray,thresh=0.08, minPoints=100000, maxIteration=200)

plik1 = open("C:\\Users\\ara22\\Desktop\\k4.xyz", "w")
for i in zb4: #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(pArray[i][0]) + " " + str(pArray[i][1]) + " " + str(pArray[i][2]) + "\n")
plik1.close()

pArray = np.delete(pArray,zb4,axis=0)
print("4")
print(str(be4))

be5,zb5 = ransac3d.fit(pArray,thresh=0.08, minPoints=100000, maxIteration=200)

plik1 = open("C:\\Users\\ara22\\Desktop\\k5.xyz", "w")
for i in zb5: #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(pArray[i][0]) + " " + str(pArray[i][1]) + " " + str(pArray[i][2]) + "\n")
plik1.close()

pArray = np.delete(pArray,zb5,axis=0)
print("5")
print(str(be5))

be6,zb6 = ransac3d.fit(pArray,thresh=0.08, minPoints=100000, maxIteration=200)

plik1 = open("C:\\Users\\ara22\\Desktop\\k6.xyz", "w")
for i in zb6: #dodawaj poszczególne elementy listy do pliku
    plik1.write(str(pArray[i][0]) + " " + str(pArray[i][1]) + " " + str(pArray[i][2]) + "\n")
plik1.close()

print("6")
print(str(be6))