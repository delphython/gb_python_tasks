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
import matplotlib.pyplot as plt
import numpy as np
from gekko import GEKKO


def get_equation_roots():
    m = GEKKO(remote=False)
    x = m.Var(1)
    expression = -12*x**4*m.sin(m.cos(x)) - 18*x**3+5*x**2 + 10*x - 30

    m.Equation(expression == 0)
    m.solve(disp=False)
    solves = [float(x.value[0])]
    for x.value in range(-22, 22):
        m.solve(disp=False)
        solves.append(float(x.value[0]))

    x = np.array(solves)
    
    return list(np.unique(x.round(decimals=10)))


def get_function_increase_intervals():
    pass


def get_function_decrease_intervals():
    pass


def draw_graph():
    x = np.arange(-22, 22.01, 0.01)
    plt.plot(x, -12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.grid(True)
    plt.show()


def calculate_top():
    pass


def get_intervals_greater_zero():
    pass


def get_intervals_less_zero():
    pass


def main():
    # print(get_equation_roots())
    print(get_function_increase_intervals())
    print(get_function_decrease_intervals())
    print(draw_graph())
    print(calculate_top())
    print(get_intervals_greater_zero())
    print(get_intervals_less_zero())


if __name__ == "__main__":
    main()
