from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

model = Sequential()

model.add(Conv2D(32, (3,3), activation='relu',
                 input_shape=(28,28,1)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.summary()
