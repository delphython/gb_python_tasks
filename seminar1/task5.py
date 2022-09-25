'''
Задание 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
'''


def main():
    print("Введите целое число")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        print(
            (
                (int_target_number % 5 == 0) and
                (int_target_number % 10 == 0) or
                (int_target_number % 15 == 0)
            ) and int_target_number % 30 != 0
        )
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
