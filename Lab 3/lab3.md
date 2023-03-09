# Lab 3 - Pytorch and Deep Networks

## Initial Implementation

### Method

Initially, a neural network was implemented following the guidance in the [Lab 3 Notes](./Lab3_2022.pdf). The following steps were taken.

1. The `PyTorch` modules were imported.
2. The _MNIST_ dataset was downloaded and assigned to the `train`, `test`, `trainset`, and `testset` variables.
3. A class, `Net()` was created to define the architecture of the neural network. In this initial implementation, 4 layers of 64 neurons were defined, with the network having 784 inputs (number of pixels per digit) and 10 outputs (number of possible digits, {0, 1, ... , 9}). A `forward()` method was also defined, which computes the output of the network from an input `x`. The `forward()` method is implemented using the _sigmoid_ function as the activation function. A _softmax_ function is also applied.
4. The `Net()` class was initilaised, and the model was trained. To do this an optimisation method was setup, for this network _stochastic  gradient descent (SGD)_ was used. The network outputs were then calculated, and from then the loss function was setup. A _cross entropy loss function_ was used. Gradient with respect to the loss function was then calculated and network parameters were finally updated.
5. The trained network was then tested on a testset, and an accuracy value was calculated.

### Results

Initially, an accuracy of 0.1 was obtained. The model was retrained multiple times, resulting in a spread of accuracy values of 0.1 += 0.005.

The `epoch` count was updated from 3 to 10, leading to a considerably longer train time. However the accuracy remained the same (0.105).
