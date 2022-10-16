"""
Задание 1. Напишите программу вычисления арифметического
выражения заданного строкой. Используйте операции +,-,/,*
приоритет операций стандартный.
"""


from fractions import Fraction


def isComplex(value):
    return (
        isinstance(value, complex) 
        # and (complex(value).imag != 0)
    )


def isRational(value):
    return (
        len(value.split("/")) == 2
    )


def calculate(
    first_number,
    second_number,
    operator,
    number_type
    ):
    operator_function = {
        "-": lambda x, y: x - y,
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    operation = operator_function[operator]

    if number_type == 1:
        return operation(
            complex(first_number),
            complex(second_number)
        )
    
    first_number_parts = first_number.split("/")
    second_number_parts = second_number.split("/")
    return operation(
        Fraction(int(first_number_parts[0]), int(first_number_parts[1])),
        Fraction(int(second_number_parts[0]), int(second_number_parts[1]))
    )


def main():

    print("Калькулятор комплексных и рациональных чисел")
    
    print("Введите первое число")
    first_number = input()

    print("Введите второе число")
    second_number = input()

    print("Введите действие (+, -, *, /)")
    operator = input()

    print(isComplex(first_number), isComplex(second_number))

    if isComplex(first_number) and isComplex(second_number):
        print(
            calculate(
                first_number,
                second_number,
                operator,
                1
            )
        )
    elif isRational(first_number) and isRational(second_number):
        print(
            calculate(
                first_number,
                second_number,
                operator,
                2
            )
        )
    else:
        print(
            "Введены не комплексные или не рациональные числа"
        )


if __name__ == "__main__":
    main()
