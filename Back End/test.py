from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import NumPy as np
import logging

logger = tf.get_logger()
logger.setLevel(logging.ERROR)

celsius_q = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
farheneit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

for i, c in enumerate(celsius_q):
    print("{} degrees Celsius = {} degrees farenheit".format(c, farheneit_a[i]))

slope = 1
intercept = 1

learning_rate = 0.1

'''
for i in range(epochs):
    curr_values = []
    for c in celsius_q:
        curr_values.append(slope*celsisu+slope)
    for i in range(len(curr_values)):
        error = curr_values[i]-celsius_q[i]
    
'''

# creating the underlying neural network to identify the relationships
IO = tf.keras.layers.Dense(units=1,input_shape=1)
# assembling the specified layers into a model
model = tf.keras.sequential([IO])
# compiling the model based on the loss and optimizer functions
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizer.Adam(learning_rate))
# training the model
history = model.fit(celsius_q, farheneit_a, epochs=500, verbose=False)

print("Finished training the model.")