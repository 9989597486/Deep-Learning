from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

model = Sequential()

model.add(SimpleRNN(16, input_shape=(5,1)))
model.add(Dense(1))

model.summary()
