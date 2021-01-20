import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from Derivative import Derivative

x, dx = symbols('x dx')
function_to_derive = np.power(3, x)
expected_value = 59049*np.log(3)
point_where_calculate = 10

expected_value_name = f"expected value = {expected_value}"
test_points = np.arange(2, 0.01, -0.0001)

numerical_results = []
analytical_results = []

is_first_nm = True
is_first_an = True

derivative = Derivative()

an_function = derivative.calculate_in_point_analytical_method(function_to_derive).subs(x, point_where_calculate)

fig = plt.figure()
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
for test_point in test_points:

    # Calculate values for two different methods
    nm_result = derivative.calculate_in_point_numerical_method(function_to_derive,
                                                               point_where_calculate, test_point)
    an_result = float(an_function.subs(dx, test_point))

    # Add results to lists
    numerical_results.append(nm_result)
    analytical_results.append(an_result)

    if np.isclose(nm_result, expected_value, 0.0001) and is_first_nm:
        ax1.vlines(x=test_point, ymin=0.9 * expected_value, ymax=1.1 * expected_value,
                   label=f'First convergence nm_result {test_point}', color="g")
        is_first_nm = False
    if np.isclose(an_result, expected_value, 0.0001) and is_first_an:
        ax2.vlines(x=test_point, ymin=0.9 * expected_value, ymax=1.1 * expected_value,
                   label=f'First convergence an_result {test_point}', color="m")
        is_first_an = False

ax1.plot(test_points, numerical_results, label="numeric DF values")
ax2.plot(test_points, analytical_results, label=f"${printing.latex(an_function)}$")
ax1.hlines(y=expected_value, xmin=test_points[0], xmax=test_points[-1], linestyles="--", color="k",
           label=expected_value_name)
ax2.hlines(y=expected_value, xmin=test_points[0], xmax=test_points[-1], linestyles="--", color="k",
           label=expected_value_name)
ax1.set_xlim([test_points[0], test_points[-1]])
ax2.set_xlim([test_points[0], test_points[-1]])

ax1.legend()
ax2.legend()

ax.set_xlabel("DF delta X")

ax.set_ylabel("Derivative result")
latex_string = printing.latex(function_to_derive)
title = f"Comparison for function = ${latex_string}$, at point {point_where_calculate}"

ax.set_title(title)
plt.savefig(title + ".png")
plt.show()
