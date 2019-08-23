import tensorflow as tf
import numpy as np
from tensorflow import keras
model = keras.sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([1,2,3,4,5], dtype=float)
ys = np.array([100,150,200,250,300], dtype=float)
model.fit(xs, ys,epochs=500)
print(model.predict([7.0]))