# Laboratory 1 – Neural Networks Basics
# In this class we are going to learn the basics of neural networks and their underlying principles.
# Objectives of this class:
#   1. Understand and code a simple neuron
#   2. Understand how a neuron learns
#   3. Understand its limitations


import numpy as np

W = np.random.randn(1, 2)
B = np.random.randn(1)

# Activation Function


def sigm(X, W, B):
    """
    Sigmoid Function, a type of activation function
    X = inputs
    W = weights
    B = bias
    """
    M = 1/(1 + np.exp(-(X.dot(W.T) + B)))
    return M

# Update rules for weights and bias


def diff_W(X, Z, Y, B, W):
    """
    Update function for weights
    """
    # Calculate the derivative of the sigmoid function
    dS = sigm(X, W, B) * (1 - sigm(X, W, B))

    # Calculate the derivative of W
    dW = (Y - Z) * dS

    # Return the dot product of the inputs and weights'
    return X.T.dot(dW)


def diff_B(X, Z, Y, B, W):
    """
    Update function for biases
    """
    # Calculate the derivative for the sigmoid function
    dS = sigm(X, W, B) * (1 - sigm(X, W, B))

    # Calculate the derivative of B
    dB = (Y - Z) * dS

    return dB.sum(axis=0)


# Sample data generation
# Training data
X_train = np.random.randint(2, size=[15, 2])
Y_train = np.array([X_train[:, 0] | X_train[:, 1]]).T

# Test data
X_test = np.random.randint(2, size=[15, 2])
Y_test = np.array([X_test[:, 0] | X_test[:, 1]]).T

# Learning process
learning_rate = 0.01

for epoch in range(500):
    output = sigm(X_train, W, B)
    
    W += learning_rate * diff_W(X_train, output, Y_train, B, W).T
    B += learning_rate * diff_B(X_train, output, Y_train, B, W)