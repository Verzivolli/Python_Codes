# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:46:24 2018

@author: Ani
"""

# Similar to IMDB classification but with 46 class output
# Output dimensionality is 46

### Importing Reuters Dataset of keras
from keras.datasets import reuters
import os

# specifying dataset path
dataset_folder_UTS = r"F:\LOT 1\Ani\Box_Sync\Notes\Deep_learning\datasets"
dataset_folder = r"D:\BoxPurrelySync\Notes\Deep_learning\datasets"
dataset_name = "imdb.npz"
dataset_path = os.path.join(dataset_folder, dataset_name)
# dataset_path = os.path.join(dataset_folder, dataset_name)

### Downloading the dataset
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(path=dataset_path, num_words = 10000)

# print(len(train_data)) # 8982
# print(len(test_data)) # 2246
# print(train_data[0]) #[1, 2, 2, 8, 43, 10, 447, 5, 25, 207, 270, 5, 3095, 111, 16, 369, 186, 90, 67, 7, 89, 5, 19, 102, 6, 19, 124, 15, 90, 67, 84, 22, 482, 26, 7, 48, 4, 49, 8, 864, 39, 209, 154, 6, 151, 6, 83, 11, 15, 22, 155, 11, 15, 7, 48, 9, 4579, 1005, 504, 6, 258, 6, 272, 11, 15, 22, 134, 44, 11, 15, 16, 8, 197, 1245, 90, 67, 52, 29, 209, 30, 32, 132, 6, 109, 15, 17, 12]

### Reverse encoded review.
word_index = reuters.get_word_index()
# out of function not to be called everytime the function is triggered
def decode_review(review):
    reverse_word_index = dict(
            [(value, key) for (key, value) in word_index.items()])
    decoded_review = ' '.join(
            [reverse_word_index.get(i - 3, '?') for i in review])
    # indexes are ofsseted by 3 becouse 3 first items of dictionary are generic #
    # padding, start of sequence, unkown
    return decoded_review

# print(decode_review(train_data[0])) # ? ? ? to just br loved and you i've set and broke many was friends seems him see of how and with movies a with know that him see people film guess are of if the some to okay from without old a though a into in that film thing in that of if is scarecrow outside days a found a looks in that film these about in that was to thought 100 him see good he without be all man a character that as it
    
###########################################
# Preparing the data
###########################################

### Encoding the integer sequences into a binary matrix
import numpy as np
def vectorize_sequences(sequences, dimension = 10000):
    results = np.zeros((len(sequences), dimension))
    for index, sequence in enumerate(sequences):
        results[index, sequence] = 1
        # sequence is an integer corresponding to word integer therefore the word column
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

# print(x_train[0])
# print(type(train_labels[0])) # numpy.int64

### Should also vectorize the labels
def to_one_hot(labels, dimension = 46):
    results = np.zeros((len(labels), dimension))
    for index, label in enumerate(labels):
        results[index, label] = 1
        # sequence is an integer corresponding to word integer therefore the word column
    return results


one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)
# Keras built in function
'''
from keras.utils.np_utils import to_categorical
one_hot_train_labels = to_categorical(train_labels)
'''

###########################################
# Building the network
###########################################

from keras import models
from keras import layers

# relu # output = dot(W, input) + b # optimizes Weights and biases
def model_builder(input_shape,
                  hidden_layers = 2, hidden_layers_units = 64, hidden_layers_activation = 'relu',
                  output_neurons = 46, output_activation = 'softmax',
                  optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy']):
    model = models.Sequential()
    # Adding hidden layers
    for i in range(hidden_layers):
        if i == 0:
            model.add(layers.Dense(hidden_layers_units, activation = hidden_layers_activation, input_shape = input_shape))
        else:
            model.add(layers.Dense(hidden_layers_units, activation = hidden_layers_activation))
    # Adding Output layers
    model.add(layers.Dense(output_neurons, activation = output_activation))
    # Compling the model
    model.compile(optimizer = optimizer, loss = loss, metrics = metrics)
    # Return
    return model

model = model_builder(input_shape = (10000, ))

###########################################
# Validating our approach
###########################################

### Creating validation set composed of 10k rows
x_val = x_train[:1000] # 1k first rows
partial_x_train = x_train[1000:]
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]

### Training the model
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs = 20,
                    batch_size = 512,
                    validation_data = (x_val, y_val))



### Plotting the training and validation loss
history_dict = history.history
# print(history_dict.keys())
import matplotlib.pyplot as plt
plt.clf() # clear plot
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(history_dict['acc']) + 1)

plt.plot(epochs, loss_values, 'bo', label = 'Training loss')
plt.plot(epochs, val_loss_values, 'b', label = 'Validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

### Plotting the training and validation loss
# clearing the plot
plt.clf() # clears the plot
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']

plt.plot(epochs, acc_values, 'bo', label = 'Training accuracy')
plt.plot(epochs, val_acc_values, 'b', label = 'Validation accuracy')
plt.title('Training and Validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

#### The network begins to overfit after 9 epochs
resutls = model.evaluate(x_test, one_hot_test_labels)
# print(results) # [0.7724950464767217, 0.8522]

### Retrain the network for 9 epochs
model = model_builder(input_shape = (10000, ))
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs = 9,
                    batch_size = 512,
                    validation_data = (x_val, y_val))
resutls = model.evaluate(x_test, one_hot_test_labels)
# print(results) # [0.7724950464767217, 0.8522]

###########################################
# Handeling the predictions
###########################################

predictions = model.predict(x_test)
print(predictions[0].shape) # (46,)
print(np.sum(predictions[0])) # 0.9999999 # 1
print(np.argmax(predictions[0])) # 3