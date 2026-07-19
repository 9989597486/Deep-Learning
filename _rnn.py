from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential()

model.add(LSTM(32, input_shape=(5,1)))
model.add(Dense(1))

model.summary()
