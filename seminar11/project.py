"""
f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
Определить корни
Найти интервалы, на которых функция возрастает
Найти интервалы, на которых функция убывает
Построить график
Вычислить вершину
Определить промежутки, на котором f > 0
Определить промежутки, на котором f < 0
"""


from scipy.optimize import fsolve
import numpy as np


def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30


def get_equation_roots():
    return fsolve(f, 0)

def get_function_increase_intervals():
    pass


def get_function_decrease_intervals():
    pass


def draw_graph():
    pass


def calculate_top():
    pass


def get_intervals_greater_zero():
    pass


def get_intervals_less_zero():
    pass


def main():
    # expression = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30

    print(get_equation_roots())
    print(get_function_increase_intervals())
    print(get_function_decrease_intervals())
    print(draw_graph())
    print(calculate_top())
    print(get_intervals_greater_zero())
    print(get_intervals_less_zero())


if __name__ == "__main__":
    main()
