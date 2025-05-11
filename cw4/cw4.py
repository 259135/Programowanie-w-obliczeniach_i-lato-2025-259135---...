import skimage.io
import skimage.feature
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import os
import math
import pandas as pd


#funkcja wycinająca próbki tekstur:
# zdjęcie - tablica ndarray z odczytaną teksturą,
# bok - długość boku próbki,
# maxIlośćPróbek - maksymalna ilość próbek do wycięcia,
# ścieżka - ścieżka do folderu, do którego zapisać próbki.
def utwórzPróbki(zdjęcie, bok, maxIlośćPróbek, ścieżka):
    wymiary = zdjęcie.shape #pobranie wymiarów tekstury
    ilośćX = int(wymiary[0]/bok) #ilość próbek w wymiarze X
    ilośćY = int(wymiary[1]/bok) #ilość próbek w wymiarze Y

    for i in range(0,ilośćX):#dla każdej pozycji w wym. X,
        for j in range(0,ilośćY):#i dla każdej pozycji w wym. Y,
            numerPróbki = j+ilośćY*i #określ numer próbki
            #print(str(i) + ", " + str(j))
            temp = zdjęcie[i*bok:(i+1)*bok,j*bok:(j+1)*bok] #wytnij próbkę
            #skimage.io.imsave(ścieżka + "probka" + str(numerPróbki) + ".jpg", temp) #zapisz próbkę pod nazwą zawierającą jej numer
            if numerPróbki+1 >= maxIlośćPróbek: # jeśli przekroczono maks. ilość próbek, przerwij wiersz
                break
        if numerPróbki + 1 >= maxIlośćPróbek: # i przerwij kolumny
            break

listaTekstur = ["mebel", "gres", "tynk"]

#tworzenie próbek dla trzech tekstur
for s in listaTekstur:
    tekstura = skimage.io.imread(listaTekstur[0] + "/" + listaTekstur[0] + ".jpg") #odczyt tekstury
    utwórzPróbki(tekstura, 128, 50, listaTekstur[0] + "/") #tworzenie tekstur

#definicja parametrów analizy GLCM
odległości = [1,3,5]
kąty = [0,math.pi/4,math.pi/2,math.pi*3/4]
parametry = ["dissimilarity", "correlation", "contrast", "energy", "homogeneity", "ASM"]

#otwarcie pliku, do którego zostaną zapisane cechy próbek
plik = open("dane.csv", 'w')
#zapis nagłówka
plik.write("dis_1_0,dis_1_45,dis_1_90,dis_1_135,dis_3_0,dis_3_45,dis_3_90,dis_3_135,dis_5_0,dis_5_45,dis_5_90,dis_5_135,cor_1_0,cor_1_45,cor_1_90,cor_1_135,cor_3_0,cor_3_45,cor_3_90,cor_3_135,cor_5_0,cor_5_45,cor_5_90,cor_5_135,cont_1_0,cont_1_45,cont_1_90,cont_1_135,cont_3_0,cont_3_45,cont_3_90,cont_3_135,cont_5_0,cont_5_45,cont_5_90,cont_5_135,ene_1_0,ene_1_45,ene_1_90,ene_1_135,ene_3_0,ene_3_45,ene_3_90,ene_3_135,ene_5_0,ene_5_45,ene_5_90,ene_5_135,hom_1_0,hom_1_45,hom_1_90,hom_1_135,hom_3_0,hom_3_45,hom_3_90,hom_3_135,hom_5_0,hom_5_45,hom_5_90,hom_5_135,ASM_1_0,ASM_1_45,ASM_1_90,ASM_1_135,ASM_3_0,ASM_3_45,ASM_3_90,ASM_3_135,ASM_5_0,ASM_5_45,ASM_5_90,ASM_5_135,klasa\n")

#obliczanie cech
for t in listaTekstur:#dla każdej tekstury
    for n in range(len(os.listdir(t + "/"))-1):#dla każdej próbki
        próbka = skimage.io.imread(t + "/" + "probka" + str(n) + ".jpg",as_gray=True)#odczytaj próbkę (jeśli odczytano jako odcienie szarości, typ danych to float z zakresu [0; 1])
        próbka = próbka * 64 # przeskaluj przez UINT5_T_MAX
        próbka = próbka.astype(np.uint8) #rzutuj na typ uint
        P = skimage.feature.graycomatrix(próbka,odległości,kąty)# oblicz macierz zdarzeń

        #dla każdej cechy
        for p in parametry:
            par = skimage.feature.graycoprops(P, prop=p)#wyznacz cechy próbki
            for k in range(len(odległości)):#dla każdej odległości,
                for l in range(len(kąty)):# i dla każdego kąta
                    plik.write(str(par[k][l]) + ",") #zapisz liczbę do pliku *.csv
        plik.write(t + "\n")#na koniec danych próbki dopisz etykietę klasy i przejdź do nowej linii

#zamknij plik
plik.close()

#odczytaj uprzednio wygenerowany plik
wektory = pd.read_csv("dane.csv", sep=',')

#rzutuj na typ np.array
wektory = np.array(wektory)


X = (wektory[:,:-1]).astype("float64") #odcięcie etykiety danych - przygotowanie "anonimowego" wektora cech
Y = wektory[:,-1] # przygotowanie wektora zawierającego tylko etykiety

#powołanie obiektu klasyfikatora (sklearn.svm)
klasyfikator = svm.SVC(gamma="auto")

#podział próbek na zbiór treningowy i testowy przy pomocy funkcji z sklearn.model_selection. Wielkość próby treningowej to 33% całości próbek
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.33)

#trenowanie klasyfikatora
klasyfikator.fit(x_train, y_train)

#predykcja
y_pred = klasyfikator.predict(x_test)

#obliczenie dokładności trafień
dokładność = accuracy_score(y_test, y_pred)
print(dokładność)

#macierz pomyłek - obliczenie przy pomocy modułu sklearn.metrics, w postaci znormalizowanej do 1
cm = confusion_matrix(y_test, y_pred, normalize="true")
print(cm)

