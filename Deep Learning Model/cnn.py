import keras 
import numpy as np

train = np.load('train.npy', allow_pickle=True)
size = 100

x_train = []
y_train = []


for i, j in train:
  x_train.append(i)
  y_train.append(j)


del train


x_train = np.array(x_train)
x_train = x_train/255.0
x_train = x_train.reshape(-1, size, size, 1)

y_train = np.array(y_train)

model = keras.Sequential()


#Conv
model.add(keras.layers.Conv2D(128, (3,3), activation='relu', input_shape=(size, size, 1)))

#Pooling: Agrupamento. Reduz o mapa de features resultante
model.add(keras.layers.MaxPool2D(2,2))

#Conv
model.add(keras.layers.Conv2D(64, (3,3), activation='relu'))

#Pooling: Agrupamento. Reduz o mapa de features resultante
model.add(keras.layers.MaxPool2D(2,2))

#Conv
model.add(keras.layers.Conv2D(32, (3,3), activation='relu'))

#Pooling: Agrupamento. Reduz o mapa de features resultante
model.add(keras.layers.MaxPool2D(2,2))


#Flatten: Achatamento. Converte a estrutura 2D em 1D
model.add(keras.layers.Flatten())

#Fully Conected
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(3, activation='softmax'))

callback = keras.callbacks.EarlyStopping(patience=2)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=30, shuffle=True, verbose=2, batch_size=16, callbacks=[callback])
model.save('cnn_xray_model.h5')


'''---------------------TESTING--------------------------'''

'''
test = np.load('test.npy', allow_pickle=True)

x_test = []
y_test = []

for i, j in test:
  x_test.append(i)
  y_test.append(j)

x_test = np.array(x_test)
x_test = x_test/255.0
x_test = x_test.reshape(-1, size, size, 1)

y_test = np.array(y_test)
y_pred = model.predict_classes(x_test)

from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
'''