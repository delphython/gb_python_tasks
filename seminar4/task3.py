'''
Задание 3. Задайте два числа. Напишите программу,
которая найдёт НОК (наименьшее общее кратное) 
этих двух чисел.
'''


import numpy


def get_input_values():
    print("Введите первое число")
    first_number = input()

    print("Введите второе число")
    second_number = input()

    return first_number, second_number


# НОД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# НОК
def lcm(a, b):
    return a * b / (gcd(a, b))


def main():
    output_str = "Введены неверные значения чисел"
    input_values = get_input_values()

    if all(input_value.isdigit() for input_value in input_values):
        first_number, second_number = list(map(int, input_values))

        output_str = (
            f"""НОК =  {lcm(first_number, second_number)} (функция)
            НОК =  {numpy.lcm(first_number, second_number)} (модуль)"""
        )

    print(output_str)


if __name__ == "__main__":
    main()
