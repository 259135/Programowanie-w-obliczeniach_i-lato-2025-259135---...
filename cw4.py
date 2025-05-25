import numpy as np
from keras import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

wektory = pd.read_csv("cw4/dane.csv", sep=',')
wektory = np.array(wektory)
X = (wektory[:,:-1]).astype("float64") #odcięcie etykiety danych - przygotowanie "anonimowego" wektora cech
Y = wektory[:,-1] # przygotowanie wektora zawierającego tylko etykiety
integer_labeller = LabelEncoder()
Y_int = integer_labeller.fit_transform(Y)
onehot_labeller = OneHotEncoder(sparse_output=False)
Y_int = Y_int.reshape(len(Y_int),1)
Y_onehot = onehot_labeller.fit_transform(Y_int)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y_onehot, test_size=0.3)

network = Sequential()
network.add(Dense(10, input_dim=72, activation='sigmoid'))
network.add(Dense(3, activation='softmax'))
network.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
network.fit(X_train, Y_train, epochs=100, batch_size=10, shuffle=True)

y_pred = network.predict(X_test)
y_pred_int = np.argmax(y_pred, axis=1)
y_test_int = np.argmax(Y_test, axis=1)
cm = confusion_matrix(y_test_int, y_pred_int)
print(cm)