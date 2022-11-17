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


import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, diff, nsolve, Eq, sin, cos


def get_function_derivative(m, expression, value):
    m.Equation(expression.dt())
    m.options.IMODE = 4
    m.solve(disp=False) 


def get_equation_roots(x, expression):
    roots = []

    start = -22
    stop = 22
    step = 0.1
    current = start

    for x0 in np.arange(current, stop + step, step):
        if x0 < current:
            continue
        sol = nsolve(expression, x, x0, verify=False)
        if sol is None:
            continue
        current = sol
        if (sol not in roots) and (sol >= start and sol <= stop):
            roots.append(sol)
    
    return roots


def get_function_increase_decrease_intervals(x, expression):
    increase_intervals = []
    decrease_intervals = []
    interval = [None, None]
    start = -22
    stop = 22
    step = 0.1

    for x0 in np.arange(start, stop + step, step):
        derr = expression.subs(x, x0)
        if derr > 0:
            if not interval[0]:
                interval[0] = [x0, derr]
                tmp_d = derr
            elif not interval[1]:
                if tmp_d < 0:
                   interval[1] = [x0, tmp_d]
        elif derr < 0:
            if not interval[0]:
                interval[0] = [x0, derr]
                tmp_d = derr
            elif not interval[1]:
                if tmp_d > 0:
                   interval[1] = [x0, tmp_d]
        if interval[0] and interval[1]:
            if interval[0][1] > 0 and interval[1][1] > 0:
                increase_intervals.append([interval[0][0], interval[1][0]])
                interval = [None, None]
            elif interval[0][1] < 0  and interval[1][1] < 0:
                decrease_intervals.append([interval[0][0], interval[1][0]])
                interval = [None, None]
        
    return increase_intervals, decrease_intervals


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
    x = Symbol('x')
    expression = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30
    fd = diff(expression)
    
    print(get_equation_roots(x, expression))
    print(get_function_increase_decrease_intervals(x, expression))
    print(get_function_increase_decrease_intervals(x, fd))
    # print(calculate_top())
    draw_graph()


if __name__ == "__main__":
    main()
