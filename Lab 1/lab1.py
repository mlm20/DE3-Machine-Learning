import numpy as np

W = np.random.randn(1, 2)
B = np.random.randn(1)


def sigm(X, W, B):
    """
    Sigmoid Function, a type of activation function
    X = inputs
    W = weights
    B = bias
    """
    M = 1/(1 + np.exp(-(X.dot(W.T) + B)))
    return M


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
