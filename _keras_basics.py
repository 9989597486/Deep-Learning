from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(8, input_shape=(4,), activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.summary()
