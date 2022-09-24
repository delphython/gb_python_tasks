'''
Задание 2. Найти максимальное из пяти чисел.
'''


def get_input_values():
    input_values = []
    for input_value_count in range(5):
        print(f"Введите число {input_value_count+1}")
        input_values.append(input())

    return input_values


def main():
    output_str = "Введены неверные значения чисел"
    input_values = get_input_values()

    if all(input_value.isdigit() for input_value in input_values):
        output_str = (f"Маскимальным из введенных чисел является число {max(input_values)}")

    print(output_str)


if __name__ == "__main__":
    main()
