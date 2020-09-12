#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:38:31 2020

@author: Mritunjay Kumar
@Question: 4 (Forward & Backward propagation Neural Network)
"""

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

# Manual Sigmoid Function
def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

# Manual Sigmoid Derivative Function
def sigmoid_derivative(sx):
    return sx * (1 - sx)

# Mean Square Error
def mse(predicted, truth):
    return np.square(predicted - truth).mean()

# Derivative of Mean Square Error
def mse_derivative(predicted, truth):
    return 2 * (predicted - truth)

# Random inputs for X and Y between 0 and 1
X = np.random.random(size=(4,2))
Y = np.random.random(size=(4,1))

# Define the shape of the weight vector.
num_data, input_dim = X.shape

# Lets set the dimensions for the 3 intermediate layers i.e hidden layer
hidden_dim1 = 4
hidden_dim2 = 4
hidden_dim3 = 4

# Define the shape of the output vector. 
output_dim = len(Y.T)

# Initialize weights between the input layer and the hidden layers.
W1 = np.random.random((input_dim, hidden_dim1))
W2 = np.random.random((hidden_dim1, hidden_dim2))
W3 = np.random.random((hidden_dim2, hidden_dim3))
W4 = np.random.random((hidden_dim3, output_dim))

# Lets take the epoches as 100 and learning rate as 0.15 on a random basis
num_epochs = 100
learning_rate = 0.15

losses = []

for epoch_n in range(num_epochs):
    layer0 = X
    
    # Forward propagation below between Input, hidden layers and Output
    layer1 = sigmoid(np.dot(layer0, W1))
    layer2 = sigmoid(np.dot(layer1, W2))
    layer3 = sigmoid(np.dot(layer2, W3))
    y_pred = sigmoid(np.dot(layer3, W4))

    # Calculate the error between predicted and Actual
    cost_error = mse(y_pred, Y)

    # Back propagation below for each layer such as:
    # Back propagation (y_pred -> layer3)
    # Error contributed by layer3 to y_pred According to weights using sigmoid derivative
    y_pred_error = mse_derivative(y_pred, Y)
    y_pred_delta = y_pred_error *  sigmoid_derivative(y_pred)

    layer3_error = mse_derivative(y_pred_delta, W4.T)
    layer3_delta = layer3_error *  sigmoid_derivative(layer3)
    
    layer2_error = mse_derivative(layer3_delta, W3.T)
    layer2_delta = layer2_error *  sigmoid_derivative(layer2)
    
    layer1_error = np.dot(layer2_delta, W2.T)
    layer1_delta = layer1_error * sigmoid_derivative(layer1)
    
    # update weights
    W4 += - learning_rate * np.dot(layer3.T, y_pred_delta)
    W3 += - learning_rate * np.dot(layer2.T, layer3_delta)
    W2 += - learning_rate * np.dot(layer1.T, layer2_delta)
    W1 += - learning_rate * np.dot(layer0.T, layer1_delta)
    
    # Log the loss value as we proceed through the epochs.
    losses.append(cost_error)
    
# Visualize the losses
plt.plot(losses)
plt.show()

print('Actual Y:', Y)
print('Predicted Y:', y_pred)