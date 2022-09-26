'''
Задание 1. По двум заданным числам проверить является
ли одно квадратом второго.
'''


def get_input_values():
    print("Введите первое число")
    first_number = input()

    print("Введите второе число")
    second_number = input()

    return first_number, second_number


def main():
    output_str = "Введены неверные значения чисел"
    input_values = get_input_values()

    if all(input_value.isdigit() for input_value in input_values):
        first_number, second_number = input_values

        tmp_str = (
            "является" if (
                int(second_number)**2 == int(first_number)
            ) else "не является"
        )
        output_str = (
            f"Число {first_number} {tmp_str} квадратом числа {second_number}"
        )

    print(output_str)


if __name__ == "__main__":
    main()
