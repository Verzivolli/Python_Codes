# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:05:13 2018

@author: Ani
"""

# Importing MNIST Dataset of keras
from keras.datasets import mnist
from keras.datasets import imdb
from keras.datasets import reuters
import os

# specifying dataset path
dataset_folder_UTS = r"F:\LOT 1\Ani\Box_Sync\Notes\Deep_learning\datasets"
dataset_folder = r"D:\BoxPurrelySync\Notes\Deep_learning\datasets"
mnist_name = "mnist.npz"
mnist_path = os.path.join(dataset_folder_UTS, mnist_name)
imdb_name = "imdb.npz"
imdb_path = os.path.join(dataset_folder_UTS, mnist_name)
reuters_name = "reuters.npz"
reuters_path = os.path.join(dataset_folder_UTS, mnist_name)
# dataset_path = os.path.join(dataset_folder, dataset_name)

imdb.load_data(path=imdb_path)
reuters.load_data(path=reuters_path)