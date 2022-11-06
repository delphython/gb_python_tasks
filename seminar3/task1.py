'''
Задание 1. Реализуйте алгоритм задания случайных чисел
без использования встроенного генератора псевдослучайных чисел.
'''

import datetime


def get_input_values():
    print("Введите начало диапазона чисел")
    first_number = input()

    print("Введите окончание диапазона чисел")
    second_number = input()

    return first_number, second_number


def get_random_int(first_number, second_number):
    random_for_gen = int(
        datetime.datetime.now().microsecond
    )

    generated = 0
    while generated < first_number or generated > second_number:
        random_for_gen /= 9
        generated = random_for_gen

    return int(round(generated))


def main():
    output_str = "Введены неверные значения чисел"
    input_values = get_input_values()

    if all(
        input_value.isdigit() for input_value in input_values
        ):
        first_number, second_number = input_values

        output_str = (
            f"""Сгенерированное число: 
            {get_random_int(int(first_number), int(second_number))}"""
        )

    print(output_str)


if __name__ == "__main__":
    main()
