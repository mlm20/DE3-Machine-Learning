# Note: This code was written by ChatGPT

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import *

# Create symbols x and y
x, y = symbols('x y')

# Ask the user for a equation
equation = input("Enter a function of x,y (e.g. x^2 + y^3): ")

# parse the user input equation to sympy expression
z = parse_expr(equation)

# Create a callable function from the sympy expression
f = lambdify((x, y), z, 'numpy')

# Create the figure and 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create x,y values
x_vals = np.linspace(-10, 10, 15)
y_vals = np.linspace(-10, 10, 15)

# Create x,y meshgrid
X, Y = np.meshgrid(x_vals, y_vals)

# Compute the z values
Z = f(X, Y)

# plot the 3D surface
ax.plot_surface(X, Y, Z)

# set x,y,z labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('z = {}'.format(equation))

# show the plot
plt.show()
