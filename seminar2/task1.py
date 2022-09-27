"""
Задание 1. Напишите программу, которая принимает на вход
число N и выдаёт последовательность из N членов..
"""


def main():
    print("Введите число N")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        for n in range(int_target_number):
            print((-3) ** n)
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
