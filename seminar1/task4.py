'''
Задание 4. Показать первую цифру дробной части числа.
'''


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
        print(target_number.split('.')[1][0])
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
