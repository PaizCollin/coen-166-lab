import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Reshape
from sklearn.metrics import confusion_matrix

fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0 #normalize the pixel values to be in [0, 1]

# Create model
model = Sequential()
model.add(Flatten(input_shape=(28,28))) # Input layer is flattened image 
model.add(Dense(10, activation='relu')) # Compressed hidden layer with P nodes + ReLU
model.add(Dense(1568, activation='relu')) # Expansion hidden layer with 28 x 28 x T, T = 2 + ReLU
model.add(Dense(784, activation='sigmoid')) # Output layer 28 x 28 + sigmoid
model.add(Reshape(target_shape=(28, 28))) # Reshape layer to 2 dimensional image

model.summary()

# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(x_train, x_train, epochs=10, batch_size=64)

x_predict = model.predict(x_test)

psnr = tf.image.psnr(x_predict, x_test, max_val=1)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, x_test)
print("Loss Rate = ", test_loss)
print("Accuracy Rate = ", test_accuracy)
print("Average PSNR = ", psnr)

# Define row count and col count for image
num_row = 2
num_col = 10
num = num_row*num_col
images = x_test
new_images = x_predict

# Create figure with one image from each class
fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))

for i in range(10):
    ax = axes[0, i%num_col]
    ax.imshow(images[i], cmap='gray')
    
for i in range(10):
    ax = axes[1, i%num_col]
    ax.imshow(new_images[i], cmap='gray')
    

plt.tight_layout()
plt.show()
