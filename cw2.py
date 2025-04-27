import csv
import math
import scipy
import numpy as np
import pyransac3d
from sklearn.cluster import KMeans
from numpy.random import default_rng
rng = default_rng()

#Definicja funkcji implementującej algorytm RANSAC

#dane - tablica np.array z trójwymiarowymi danymi punktów chmury
#k - ilość iteracji algorytmu do wykonania
#t - maksymalna odległość od wylosowanej płaszczyzny, dla której punkt jest uznany za bliski
#d - minimalna ilość punktów uznanych za bliskie, dla któej następuje określenie wylosowanej płaszczyzny jako dobrze dopasowanej
def ransac(dane, k, t, d):
    iteracja=0
    najlepsze_dopasowanie = None
    najlepszy_blad = math.inf
    while iteracja<k :
        #print("Iteracja " + str(iteracja) + " z " + str(k))
        wp = rng.permutation(dane)[0:3] #wp zawiera trzy losowo wybrane punkty do wyznaczenia płaszczyzny
        a = [wp[1][0] - wp[0][0], wp[1][1] - wp[0][1], wp[1][2] - wp[0][2]] #definicja wektora a
        b = [wp[2][0] - wp[0][0], wp[2][1] - wp[0][1], wp[2][2] - wp[0][2]] #definicja wektora b

        A = a[1] * b[2] - a[2] * b[1] #obliczenie współczynnika A równania ogólnego płaszczyzny
        B = -(a[0] * b[2] - a[2] * b[0]) #obliczenie współczynnika B równania ogólnego płaszczyzny
        C = a[0] * b[1] - a[1] * b[0] #obliczenie współczynnika C równania ogólnego płaszczyzny
        D = -A * wp[0][0] - B * wp[0][1] - C * wp[0][2] #obliczenie współczynnika D równania ogólnego płaszczyzny
        axb = [A, B, C]  #ustalenie wektora normalnego do płaszczyzny określonej równaniem Ax+By+Cz+D=0
        norma=math.sqrt(pow(A, 2) + pow(B, 2) + pow(C, 2)) #obliczenie długości wektora normalnego, przydatne przy obliczaniu odległości punktu od płaszczyzny; przyspiesza obliczenia.
        dane_pozostale = []

        zaakceptowane_bliskie = []
        odleglosci_punktow_zaakceptowanych = []
        #iteracja po każdym punkcie
        for l in dane:
            dd = abs(A * l[0] + B * l[1] + C * l[2] + D)/norma #obliczenie odległości punktu l od płaszczyzny o wyliczonym równaniu
            if dd < t: #jeśli ta odległość jest mniejsza od granicznej...
                zaakceptowane_bliskie.append(l) #dołącz punkt do macierzy punktów bliskich
                odleglosci_punktow_zaakceptowanych.append(dd) #oraz dołącz odległość do odpowiedniej macierzy
            else:
                dane_pozostale.append(l) #jeśli nie, dodaj punkt do macierzy punktów dalekich
        if len(zaakceptowane_bliskie) > d: #jeśli ilość punktów bliskich jest większa od granicznej...
            aktualny_blad = np.mean(odleglosci_punktow_zaakceptowanych)   #określ błąd dopasowania, jako średnią odległość punktów bliskich od wyznaczonej płaszczyzny
            if aktualny_blad < najlepszy_blad: #jeśli błąd dla aktualnie analizowanej płaszczyzny jest mniejszy od dotychczas najmniejszego...
                najlepszy_blad = aktualny_blad #uznaj aktualny błąd za najlepszy
                najlepsze_dopasowanie = axb #oraz aktualne dopasowanie za najlepsze jak dotąd
        iteracja = iteracja + 1 #zwiększ wskaźnik iteracji
    if najlepszy_blad == math.inf: #zwróć informację, iż analizowana chmura jest płaszczyzną, jeśli udało się dopasować płaszczyznę z wymaganymi przez Użytkownika parametrami t oraz d
        czy_plaszczyzna = "nie"
    else:
        czy_plaszczyzna = "tak"

    if najlepsze_dopasowanie is not None: #jeżeli udało się dopasować jakąkolwiek płaszczyznę zgodnie z założeniami, znormalizuj wektor normalny.
        najlepsze_dopasowanie=najlepsze_dopasowanie / np.linalg.norm(najlepsze_dopasowanie)
    return najlepsze_dopasowanie, najlepszy_blad, czy_plaszczyzna, dane_pozostale, zaakceptowane_bliskie

    #zwróć:
    #najlepsze_dopasowanie - wektor normalny do najlepiej dopasowanej płaszczyzny
    #najlepszy_blad - średnią odległość wszystkich punktów od tej płaszczyzny
    #czy_plaszczyzna - tekstową informację, czy wejściowa chmura punktów była płaszczyzną
    #dane_pozostale - lista punktów dalekich
    #zaakceptowane_bliskie - lista punktów bliskich

print("Ładowanie danych")
punkty = []
sciezkaIn = input("Podaj ścieżkę odczytu chmury punktów, zawierającą trzy zadane obiekty")
with open("C:\\Users\\ara22\\Desktop\\point.xyz", newline='\n') as plik:
    csvPunkty = csv.reader(plik, delimiter=' ')
    for row in csvPunkty:
        #formowanie tablicy punktów trójwymiarowych
        pt = []
        pt.append(float(row[0]))
        pt.append(float(row[1]))
        pt.append(float(row[2]))
        punkty.append(pt)

print("Klasteryzacja danych")
#utworzenie obiektu klasteryzatora
clusterer = KMeans(n_clusters=3)#, init=[[-1.2,-1.2,-1.2],[0,0,0],[1.2,1.2,1.2]])
pArray = np.array(punkty) #konwersja na tablicę np
y = clusterer.fit_predict(pArray) #przeprowadzenie klasteryzacji

#selekcja punktów należących do poszczególnych klastrów
klaster1 = y == 0
klaster2 = y == 1
klaster3 = y == 2
k1Punkty = pArray[klaster1]
k2Punkty = pArray[klaster2]
k3Punkty = pArray[klaster3]

print("Zapis danych klastrów")
sciezka = input("Podaj katalog do zapisu plików klastrów. Zakończ ścieżkę ukośnikiem")
sciezka1 = sciezka + "point_cl1.xyz"
sciezka2 = sciezka + "point_cl2.xyz"
sciezka3 = sciezka + "point_cl3.xyz"

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
nd1,nb1,czy1,_,_ = ransac(k1Punkty,200,0.1,0.7*len(k1Punkty))

print("Klaster nr 1:")
print("Wektor normalny: " + str(nd1))
print("Czy to płaszczyzna: " + czy1)
if czy1 =="tak":
    print("Średnia odległość punktu od płaszczyzny: " + str(nb1))
    if abs(nd1[0])<0.1 and abs(nd1[1])<0.1 and abs(nd1[2])>0.9: #jeśli tylko składowa C wektora normalnego ma wartość bliską +-1, to ta płaszczyzna jest pozioma
        print("Ta płaszczyzna jest pozioma.")
    elif abs(nd1[2])<0.1: #jeśli składowa C jest bliska zeru, to przy dowolnych wartościach składowych A i B ta płaszczyzna jest pionowa
        print("Ta płaszczyzna jest pionowa.")

print("")

print("Analiza 2. klastra...")
nd2,nb2,czy2,_,_ = ransac(k2Punkty,200,0.1,0.7*len(k2Punkty))

print("Klaster nr 2:")
print("Wektor normalny: " + str(nd2))
print("Czy to płaszczyzna: " + czy2)
if czy2 =="tak":
    print("Średnia odległość punktu od płaszczyzny: " + str(nb2))
    if abs(nd2[0])<0.1 and abs(nd2[1])<0.1 and abs(nd2[2])>0.9: #jeśli tylko składowa C wektora normalnego ma wartość bliską +-1, to ta płaszczyzna jest pozioma
        print("Ta płaszczyzna jest pozioma.")
    elif abs(nd2[2])<0.1: #jeśli składowa C jest bliska zeru, to przy dowolnych wartościach składowych A i B ta płaszczyzna jest pionowa
        print("Ta płaszczyzna jest pionowa.")
print("")

print("Analiza 3. klastra...")
nd3,nb3,czy3,_,_ = ransac(k3Punkty,200,0.1,0.7*len(k3Punkty))
print("Klaster nr 3:")
print("Wektor normalny: " + str(nd3))
print("Czy to płaszczyzna: " + czy3)
if czy3 =="tak":
    print("Średnia odległość punktu od płaszczyzny: " + str(nb3))
    if abs(nd3[0])<0.1 and abs(nd3[1])<0.1 and abs(nd3[2])>0.9: #jeśli tylko składowa C wektora normalnego ma wartość bliską +-1, to ta płaszczyzna jest pozioma
        print("Ta płaszczyzna jest pozioma.")
    elif abs(nd3[2])<0.1: #jeśli składowa C jest bliska zeru, to przy dowolnych wartościach składowych A i B ta płaszczyzna jest pionowa
        print("Ta płaszczyzna jest pionowa.")