# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:38:10 2018

@author: Ani
"""

### Importing house pricing dataset (1970)
from keras.datasets import boston_housing
import os

# specifying dataset path
dataset_folder_UTS = r"F:\LOT 1\Ani\Box_Sync\Notes\Deep_learning\datasets"
dataset_folder = r"D:\BoxPurrelySync\Notes\Deep_learning\datasets"
dataset_name = "imdb.npz"
dataset_path = os.path.join(dataset_folder, dataset_name)
# dataset_path = os.path.join(dataset_folder, dataset_name)

### Downloading the dataset
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data(path=dataset_path)

# print(train_data.shape) # (404, 13)
# print(test_data.shape) # (102, 13)
# we have 402 rows for training and 102 for testing each with 13 given numerical attributes 

###########################################
# Normalizing the data
###########################################

# it is neceseary for the data to be equaly normalized

mean = train_data.mean(axis = 0)
train_data -= mean
std = train_data.std(axis = 0)
train_data /= std

test_data -= mean
test_data /= std
# print(train_data[0])

###########################################
# Model definition
###########################################

from keras import models
from keras import layers

# relu # output = dot(W, input) + b # optimizes Weights and biases
def model_builder(input_shape = (train_data.shape[1], ),
                  hidden_layers = 2, hidden_layers_units = 64, hidden_layers_activation = 'relu',
                  output_neurons = 1, output_activation = None,
                  optimizer = 'rmsprop', loss = 'mse', metrics = ['mae']):
    # Loss = mse # Mean Squad error # Very used for regresion matrix
    # metrics = 'mae' # Mean absolute value
    # output_activation = None # linear layer that may get all values range
    model = models.Sequential()
    # Adding hidden layers
    for i in range(hidden_layers):
        if i == 0:
            model.add(layers.Dense(hidden_layers_units, activation = hidden_layers_activation, input_shape = input_shape))
        else:
            model.add(layers.Dense(hidden_layers_units, activation = hidden_layers_activation))
    # Adding Output layers
    if output_activation == None:
        model.add(layers.Dense(output_neurons))
    else:
        model.add(layers.Dense(output_neurons, activation = output_activation))
    # Compling the model
    model.compile(optimizer = optimizer, loss = loss, metrics = metrics)
    # Return
    return model

# model = model_builder()

###########################################
# Validating our approach
###########################################
##########################
# K-fold validation
##########################

import numpy as np
k = 4
num_val_samples = len(train_data) // k
num_epochs = 100
all_scores = []

for i in range(k):
    print('processing fold #', i)
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
    
    partial_train_data = np.concatenate([train_data[: i * num_val_samples],
                                        train_data[(i + 1) * num_val_samples :]])
    partial_train_targets = np.concatenate([train_targets[:i * num_val_samples],
                                           train_targets[(i + 1) * num_val_samples :]])
    model = model_builder()
    # verbose = 0 # trains the model in silent mode
    model.fit(partial_train_data, partial_train_targets, epochs = num_epochs,
              batch_size = 1, verbose = 0)
    val_mse, val_mae = model.evaluate(val_data, val_targets)
    all_scores.append(val_mae)

# all_scores # [2.051220961136393, 2.343809363865616, 2.7343281578309466, 2.3244060277938843]
# np.mean(all_scores) # 2.36344112765671

### Saving the validation logs at each fold
num_epochs = 500
all_mae_history = []

for i in range(k):
    print('processing fold #', i + 1)
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]
    
    partial_train_data = np.concatenate([train_data[: i * num_val_samples],
                                        train_data[(i + 1) * num_val_samples :]],
                                        axis = 0)
    partial_train_targets = np.concatenate([train_targets[:i * num_val_samples],
                                           train_targets[(i + 1) * num_val_samples :]],
                                            axis = 0)
    model = model_builder()
    # verbose = 0 # trains the model in silent mode
    history = model.fit(partial_train_data, partial_train_targets, epochs = num_epochs,
                        validation_data = (val_data, val_targets),
                        batch_size = 1, verbose = 0)
    all_mae_history.append(history.history['val_mean_absolute_error'])

### Plotting the validation scores
average_mae_history = [np.mean([x[i] for x in all_mae_history]) for i in range(num_epochs)]
import matplotlib.pyplot as plt
plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation mae')
plt.show()

### excluding 10 first epochs from plot

def smooth_curve(points, factor = 0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points

smooth_mae_history = smooth_curve(average_mae_history[10:])
plt.clf()
plt.plot(range(11, len(smooth_mae_history) + 11), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation mae')
plt.show()

smooth_mae_history = smooth_curve(average_mae_history[10:100])
plt.clf()
plt.plot(range(11, len(smooth_mae_history) + 11), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation mae')
plt.show()

### Retraining the model
model = model_builder()
model.fit(train_data, train_targets,
          epochs = 50, batch_size = 16, verbose = 0)
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
test_mae_score # 2.750462709688673