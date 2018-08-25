# First look at a neural network
"""
# Deep Learning Using Python
# Chapter 2
# Section 2.1

# Mnist sample digits database
"""
###########################################
# Importing MNIST Dataset of keras
###########################################

# Importing MNIST Dataset of keras
from keras.datasets import mnist
import os

# specifying dataset path
dataset_folder_UTS = r"F:\LOT 1\Ani\Box_Sync\Notes\Deep_learning\datasets"
dataset_folder = r"D:\BoxPurrelySync\Notes\Deep_learning\datasets"
dataset_name = "mnist.npz"
dataset_path = os.path.join(dataset_folder_UTS, dataset_name)
# dataset_path = os.path.join(dataset_folder, dataset_name)

# Downloading the dataset
'''
# example from keras documentation
(x_train, y_train), (x_test, y_test) = reuters.load_data(path="reuters.npz",
                                                         num_words=None,
                                                         skip_top=0,
                                                         maxlen=None,
                                                         test_split=0.2,
                                                         seed=113,
                                                         start_char=1,
                                                         oov_char=2,
                                                         index_from=3)
'''
(train_images, train_labels), (test_images, test_labels) = mnist.load_data(path=dataset_path)

# looking at Train and test dataset properties
# train_images.shape ## (60000, 28, 28)
# len(train_labels) ## 60000
train_len = len(train_labels)
# train_labels ## array([5, 0, 4,])  ###
# test_images.shape ## (60000, 28, 28)
# len(test_images) ## 60000
test_len = len(test_images)
# test_labels ## array([5, 0, 4,])  ###

###########################################
# The Network architecture
###########################################

from keras import models
from keras import layers


### To do
'''
# Make the networkk architecture created by a function
def model(layers = 1, units = [512], outputs = 2, input_shape = (28 * 28,)):
    print(type(units))

'''

network = models.Sequential()
# Dense == Fully conected layers
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
# output layer # 10 classes
network.add(layers.Dense(10, activation = 'softmax'))

network.compile(optimizer = 'rmsprop',
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])
'''
# Loss function - how the network will be able to measure performance in the training data, and thus how it will be able to steer itself in the right direction
# optimizer - the mechanism the network will update itself based on the data it sees and its loss function
# metrics to monitor during training and testing - (atm only focused on accuracy)
'''

###########################################
# Preparing the image data andlabels
###########################################

# reshaping the data from (60000, 28, 28) to (60000, 28 * 28)
train_images = train_images.reshape((train_len, 28 * 28))
test_images = test_images.reshape((test_len, 28 * 28))

# Converting array values from [0 255] to [0, 1]
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

### Preparing the labels
from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


###########################################
# Fitting the network and looking at obtained accuracy
###########################################

history = network.fit(x=train_images, y=train_labels, batch_size=128, epochs=5)

test_loss, test_accuracy = network.evaluate(x=test_images, y=test_labels)
print('test accuracy: ', test_accuracy)