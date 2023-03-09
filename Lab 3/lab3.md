# Lab 3 - Pytorch and Deep Networks

## Initial Implementation

### Method

Initially, a neural network was implemented following the guidance in the [Lab 3 Notes](./Lab3_2022.pdf). The following steps were taken.

1. The `PyTorch` modules were imported.
2. The _MNIST_ dataset was downloaded and assigned to the `train`, `test`, `trainset`, and `testset` variables.
3. A class, `Net()` was created to define the architecture of the neural network. In this initial implementation, 4 layers of 64 neurons were defined, with the network having 784 inputs (number of pixels per digit) and 10 outputs (number of possible digits, {0, 1, ... , 9}). A `forward()` method was also defined, which computes the output of the network from an input `x`. The `forward()` method is implemented using the _sigmoid_ function as the activation function. A _softmax_ function is also applied.
4. The `Net()` class was initilaised, and the model was trained. To do this an optimisation method was setup, for this network _stochastic gradient descent (SGD)_ was used. The network outputs were then calculated, and from then the loss function was setup. A _cross entropy loss function_ was used. Gradient with respect to the loss function was then calculated and network parameters were finally updated.
5. The trained network was then tested on a testset, and an accuracy value was calculated.

### Results

-   Initially, accuracies of: 0.114, 0.101, and 0.103 were obtained.

-   The `epoch` count was updated from 3 to 10, leading to a considerably longer train time. However the accuracy (0.114) remained the same range .

## Alternative Implementation

### ReLu Activation Function

#### Method

The `epoch` count was retuned to 3, and the activation function was changed from `sigmoid` to `relu`.

#### Results

The network was trained and tested three times, the accuracies were: 0.101, 0.138, and 0.103. This is a slight improvement from the `sigmoid` function.

### Adam Optimiser

#### Method

The ReLu activation function was kept, and the optimiser  from  stochastic  gradient  descent  to  Adam.

#### Results

Using the `Adam` optimiser, the accuracies were: 0.941, 0.858, and 0.941. This is a serious improvement in accuracy compared to the previous method. However, Adam was also far more time consuming than gradient descent, taking up to 1m 26.5s for 3 epochs, compared to ~36s for gradient descent.

### Additional Hidden Layer

#### Method
An additional hidden layer was added to the neural network.
#### Results
This resulted in an accuracy of 0.857. This roughly the same as without the extra layer.

### Additional Neurons

#### Method
The additional hidden layer was removed since it was ineffective. However the number of neurons in each layer was increased from 64 to 128.

#### Results
This resulted in an accuracy of 0.842. Hence adding additional neurons was also ineffective.