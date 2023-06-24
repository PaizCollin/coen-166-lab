import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from sklearn.metrics import confusion_matrix


fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0 #normalize the pixel values to be in [0, 1]

# Define row count and col count for image
num_row = 2
num_col = 5
num = num_row*num_col
images = x_train
classes = y_train
i = 0
j = 0

# Create figure with one image from each class
fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
while j < 10:
    if(j == classes[i]):
        ax = axes[j//num_col, j%num_col]
        ax.imshow(images[i], cmap='gray')
        ax.set_title('Class: {}'.format(classes[i]))
        j = j + 1
    i = i + 1
plt.tight_layout()
plt.show()

# Create model
model = Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Loss Rate = ", test_loss)
print("Accuracy Rate = ", test_accuracy)

# Calculate predictions
probability = model.predict(x_test)
y_test_hat = np.argmax(probability, axis=1)
cm = confusion_matrix(y_test, y_test_hat, labels=range(10))