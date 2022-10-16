"""
Задание 1. Напишите программу вычисления арифметического
выражения заданного строкой. Используйте операции +,-,/,*
приоритет операций стандартный.
"""


def calculate(expression):
    operator_function = {
        "-": lambda x, y: x - y,
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    numbers = []
    operators = []

    elements = list(f"({expression})")

    while elements:
        element = elements.pop(0)

        if element.isdecimal():
            numbers.append(float(element))
        elif element == ")":
            operator = operators.pop()
            while operators and operator != "(":
                x, y = numbers.pop(), numbers.pop()
                f = operator_function[operator]
                numbers.append(f(x, y))

                operator = operators.pop()
        else:
            operators.append(element)

    return numbers[0]


def main():
    print("Введите арифметическое выражение")
    arithmetic_expression = input()
    print(calculate(arithmetic_expression))


if __name__ == "__main__":
    main()
