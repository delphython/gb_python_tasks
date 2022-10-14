'''
Задание 6. Реализуйте алгоритм задания случайных чисел
без использования встроенного генератора псевдослучайных чисел.
'''

import datetime
from random import seed


def get_input_values():
    print("Введите начало диапазона чисел")
    first_number = input()

    print("Введите окончание диапазона чисел")
    second_number = input()

    return first_number, second_number


def get_random_int(first_number, second_number):
    second_number_len = len(str(second_number))
    divider = int(f"1{'0'*second_number_len}")

    random_for_gen = int(
        str(
            datetime.datetime.now().microsecond
        )[0:second_number_len]
        )
    
    while(True): 
        if (random_for_gen >= first_number and 
        random_for_gen <= second_number):
            break
                
        random_for_gen = (
            (random_for_gen / divider) *
            (second_number - first_number) +
            first_number
        )
    
    return int(round(random_for_gen))


# Для общего развития
def pseudorandom_number_generator(
    seed,
    n,
    a=1664525,
    c=1013904223,
    m=2**32
):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers


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
