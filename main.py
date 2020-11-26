from Derivative import Derivative
import numpy as np
import matplotlib.pyplot as plt

function_to_integrate = "3*np.power(x,3)"
expected_value = 900
expected_value_name = f"expected value = {expected_value}"

test_points = np.arange(5, 0.01, -0.01)
point_where_calculate = 10
df_results = []
is_first = True
derivative = Derivative()
for test_point in test_points:

    df = derivative.calculate_in_point(function_to_integrate, point_where_calculate, test_point)
    df_results.append(df)

    if np.isclose(df, expected_value, 0.005) and is_first:
        plt.vlines(x=test_point, ymin=0, ymax=expected_value + 0.1,
                   label=f'First convergence df {test_point}', color="g")
        is_first = False

plt.plot(test_points, df_results, label="DF values")
plt.hlines(y=expected_value, xmin=test_points[0], xmax=test_points[-1], linestyles="--", color="k",
           label=expected_value_name)
plt.xlim(test_points[0], test_points[-1])
plt.legend()
plt.xlabel("DF steps done")
plt.ylabel("Derivative result")
title = f"Comparison for function = {function_to_integrate}, at point {point_where_calculate}"

plt.title(title)
plt.savefig(title + ".png")
plt.show()
