import numpy as np
import parser


class Derivative:

    def calculate_in_point(self, function_to_integrate, point_where_calculate, delta_x):
        st = parser.expr(function_to_integrate)
        code = st.compile('Derivative.py')
        x = point_where_calculate + delta_x
        y_2 = eval(code)
        x = point_where_calculate - delta_x
        y_1 = eval(code)
        return (y_2 - y_1) / (2 * delta_x)


if __name__ == '__main__':
    derivative = Derivative()
    print(derivative.calculate_in_point("3*np.power(x,3)", 10, 0.1))
