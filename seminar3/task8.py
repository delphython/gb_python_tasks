"""
Задание 8. Напишите программу, которая будет
преобразовывать десятичное число в двоичное.
"""


def get_fibonacci(input_number):
    if input_number in (1, 2):
        return 1
    return (
        get_fibonacci(input_number - 1) +
        get_fibonacci(input_number - 2)
    )


def get_negafibonacci(input_number):
    return (
        (
            (-1) ** (abs(input_number) + 1))
            ) * get_fibonacci(abs(input_number)
    )


def main():
    print("Введите число")
    target_number = input()

    if target_number.isdigit():
        fib_list = [get_fibonacci(i) for i in range(1, int(target_number)+1)]
        negafib_list = [
            get_negafibonacci(i) for i in range(-1, -int(target_number)-1, -1)
        ]

        print(negafib_list[::-1] + [0] + fib_list)
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
