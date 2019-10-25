# -*- coding: utf-8 -*-
"""
Author: Ani Verzivolli
"""

###########################
### Overfitting and underfitting
###########################

###########################
# Code from "IMDB_Classifier_ANN.py"
###########################

### Importing IMDB Dataset of keras
from keras.datasets import imdb
import os

# specifying dataset path
cwd = os.getcwd()
dataset_folder = "datasets"
dataset_name = "imdb.npz"
dataset_path = os.path.join(cwd,os.path.join(dataset_folder, dataset_name))
# os.listdir('.')

### Downloading the dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(path=dataset_path, num_words = 10000)


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
# print(type(train_labels[0])) # int64\

### Should also vectorize the labels
y_train = np.array(train_labels).astype('float32')
y_test = np.array(test_labels).astype('float32')


###########################################
# Building the network
###########################################

from keras import models
from keras import layers

# relu # output = dot(W, input) + b # optimizes Weights and biases
def model_builder(input_shape,
                  hidden_layers = 2, hidden_layers_units = 16, hidden_layers_activation = 'relu',
                  output_neurons = 1, output_activation = 'sigmoid',
                  optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy']):
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

# Retraining the model for 3 epochs as validation graph from IMDB File recomends
model = model_builder(input_shape = (10000, ))
model.fit(x_train, y_train, epochs = 4, batch_size = 512)
results = model.evaluate(x_test, y_test)
# print(results) # [0.3076886553382874, 0.87828] # 87.8% accuracy




