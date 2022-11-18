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
from sympy import Symbol, diff, nsolve, sin, cos


def get_equation_roots(x, expression):
    roots = []

    start = -22
    stop = 22
    step = 0.1
    current = start

    for x0 in np.arange(current, stop + step, step):
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
    start = -22
    stop = 22
    step = 0.1

    x = np.arange(start, stop + step, step)
    plt.plot(x, -12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.grid(True)
    plt.show()


def main():
    x = Symbol('x')
    expression = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30
    fd = diff(expression)
    
    print("Определить корни:")
    print(",".join("%10.3f" % x for x in get_equation_roots(x, expression)))

    increase_intervals, decrease_intervals = get_function_increase_decrease_intervals(x, expression)
    
    print("Найти интервалы, на которых функция возрастает:")
    for increase_from, increase_to in increase_intervals:
        print(f"с {'%10.3f' % increase_from} по {'%10.3f' % increase_to}")
    
    print("Найти интервалы, на которых функция убывает:")
    for decrease_from, decrease_to in decrease_intervals:
        print(f"с {'%10.3f' % decrease_from} по {'%10.3f' % decrease_to}")

    more_zero_intervals, less_zero_intervals = get_function_increase_decrease_intervals(x, fd)

    print("Определить промежутки, на котором f > 0:")
    for more_zero_from, more_zero_to in more_zero_intervals:
        print(f"с {'%10.3f' % more_zero_from} по {'%10.3f' % more_zero_to}")
    
    print("Определить промежутки, на котором f < 0:")
    for less_zero_from, less_zero_to in less_zero_intervals:
        print(f"с {'%10.3f' % less_zero_from} по {'%10.3f' % less_zero_to}")
    
    print("Вычислить вершину:")
    print(",".join("%10.3f" % x for x in get_equation_roots(x, fd)))
    
    print("Построить график:")
    draw_graph()


if __name__ == "__main__":
    main()
