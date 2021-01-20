import numpy as np
import parser
from sympy import symbols, simplify


class Derivative:

    # Calculate values of function in points: x+delt_x and x-delta_x,
    # then subtract them and divide by 2*delta_X
    def calculate_in_point_numerical_method(self, function_to_integrate,
                                            point_where_calculate, delta_x):
        st = parser.expr(str(function_to_integrate))
        code = st.compile('Derivative.py')
        x = point_where_calculate + delta_x
        y_2 = eval(code)
        x = point_where_calculate - delta_x
        y_1 = eval(code)
        return (y_2 - y_1) / (2 * delta_x)

    # Create two equations. 1'st substitute each x in function by x+delta_x, 2'nd x substituted by x-delta_x.
    # Then subtract them, divide by 2*delta_x. Simplify received equation with two parameters x and delta_x.
    def calculate_in_point_analytical_method(self, function_to_integrate):
        x, dx = symbols('x dx')
        expr = function_to_integrate
        y1 = expr.subs(x, x + dx)
        y2 = expr.subs(x, x - dx)
        y = (y1 - y2) / (2 * dx)
        y = simplify(y)
        return y


if __name__ == '__main__':
    derivative = Derivative()
    x, dx = symbols('x dx')
    print(derivative.calculate_in_point_numerical_method(3 * np.power(x, 3), 10, 0.1))
    print(derivative.calculate_in_point_analytical_method(3 * np.power(x, 3), 10).subs(dx, 0.1).subs(x, 10))
