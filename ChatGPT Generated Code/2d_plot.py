# Note: This code was written by ChatGPT

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = Symbol('x')
equation = input("Enter a function of x (e.g. x^2 + 3x - 4): ")
y = parse_expr(equation)
f = lambdify(x, y, 'numpy')
f_vec = np.vectorize(f)
x_vals = np.linspace(-10, 10, 100)
y_vals = f_vec(x_vals)

plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = {}'.format(equation))
plt.show()
