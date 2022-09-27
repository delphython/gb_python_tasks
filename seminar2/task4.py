'''
Задание 4. Подсчитать сумму цифр в вещественном числе.
'''


from itertools import count


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    print("Введите вещественное число")
    target_number = input()

    if is_float(target_number):
        integer_part, fractional_part = target_number.split('.')
        print(
            f"""Сумма цифр числа {target_number} =
            {sum(map(int, integer_part)) + sum(map(int, fractional_part))}"""
        )
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
