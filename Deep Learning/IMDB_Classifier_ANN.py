# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:59:56 2018

@author: Ani
"""

###########################################
# Importing IMDB Dataset of keras
# Classifier for good or bad reviews
###########################################

### Importing IMDB Dataset of keras
from keras.datasets import imdb
import os

# specifying dataset path
cwd = os.getcwd()
dataset_folder = "datasets"
dataset_name = "imdb.npz"
dataset_path = os.path.join(cwd,os.path.join(dataset_folder, dataset_name))
# dataset_path = os.path.join(dataset_folder, dataset_name)

### Downloading the dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(path=dataset_path, num_words = 10000)
# print(len(train_data)) # 25000
# print(len(test_data)) # 25000
# Num_words 10000 argument means we will keep only the top 10000 most frequently ocurring words in the training data

first_sample_data = train_data[0]
# our data contains list of indexes of words occurred in each sample
# max([max(sequence) for sequence in train_data]) # = 9999 # no word index exceeds choosed num_words

### Reverse encoded review.
word_index = imdb.get_word_index()
# out of function not to be called everytime the function is triggered
def decode_review(review):
    reverse_word_index = dict(
            [(value, key) for (key, value) in word_index.items()])
    decoded_review = ' '.join(
            [reverse_word_index.get(i - 3, '?') for i in review])
    # indexes are ofsseted by 3 becouse 3 first items of dictionary are generic #
    # padding, start of sequence, unkown
    return decoded_review
'''
# print(decode_review(train_data[0]))
# ? this film was just brilliant casting location scenery story direction everyone's really suited the
# part they played and you could just imagine being there robert ? is an amazing actor and now the same
# being director ? father came from the same scottish 
'''


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

'''
###########
# Configuring Optimizer / losses / metrics
##########
from keras import optimizers
from keras import losses
from keras import metrics
model.compile(optimizer = optimizers.RMSprop(lr = 0.001),
                          loss = losses.binary_crossentropy,
                          metrics = [metrics.binary_accuracy])
'''
model = model_builder(input_shape = (10000, ))

###########################################
# Validating our approach
###########################################

### Creating validation set composed of 10k rows
x_val = x_train[:10000] # 10 k first rows
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

### training the model
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

# checking accuracy on test sample.
# model trained on train and validation set seperately
results = model.evaluate(x_test, y_test)
# print(results) # [0.8520382542431355, 0.855] # 85.5% accuracy

# model trained for 20 epoch on whole training set (25k row) # no validation
model = model_builder(input_shape = (10000, ))
model.fit(x_train, y_train, epochs = 20, batch_size = 512)
results = model.evaluate(x_test, y_test)
# print(results) # [0.7724950464767217, 0.8522] # 85.2% accuracy

# Retraining the model for 3 epochs as validation graph recomends
model = model_builder(input_shape = (10000, ))
model.fit(x_train, y_train, epochs = 4, batch_size = 512)
results = model.evaluate(x_test, y_test)
# print(results) # [0.3076886553382874, 0.87828] # 87.8% accuracy


'''
######
Testing Area
######
for i in range(2):
    print(i)
'''