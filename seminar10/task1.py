"""
Написать функцию-декоратор для кеширования значений функции
Написать функцию seq(n)
n = 0 ....N
(1 + n) ** n возвращает [x1, x2, x3, , , , xn]
с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)
"""


import time
from functools import wraps


def logging(func):
    def wrapper(*args):
        n = args[0]
        print(f"Run function {func.__name__} with n = {n}")
        start = time.perf_counter()
        result = func(*args)
        print(f"Time run: {time.perf_counter() - start}")
        return result
    return wrapper


def cache(func):
    cache_res = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache_res:
            cache_res[args] = func(*args)
        return cache_res[args]
    return wrapper


@logging
@cache
def seq(n):
    return [(1 + x) ** x for x in range(n)]


def main():
    print(seq(10))


if __name__ == "__main__":
    main()
