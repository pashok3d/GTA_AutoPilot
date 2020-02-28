import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import MaxPooling2D, Convolution2D, Dense, Flatten

#data_1 = np.load('training_data_1.npy')
#data_2 = np.load('training_data_2.npy')
#data = np.concatenate((data_1,data_2),axis=0)
#OR
data = np.load('training_data.npy')

#giving up list format
for i in range(np.shape(data)[0]):
    data[i][1] = data[i][1][0]

#remove 'stop' class if necessary
data = data[data[:,1] != 3]

#reshaping data
X = np.array([i[0] for i in data]).reshape(-1,100,100,1)
y = [i[1] for i in data]

#splitting data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

#encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#scaling
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Initialising the CNN
model = Sequential()
# Step 1 - Convolution
model.add(Convolution2D(32, kernel_size=3, input_shape = (100, 100, 1), activation = 'relu'))
# Step 2 - Pooling
model.add(MaxPooling2D(pool_size = (2, 2)))
# Adding a second convolutional layer
model.add(Convolution2D(16, kernel_size=3, activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
# Step 3 - Flattening
model.add(Flatten())
# Step 4 - Full connection
model.add(Dense(128, activation = 'relu'))
model.add(Dense(3, activation='softmax'))
# Compiling the CNN
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

model.save("model.h5")

