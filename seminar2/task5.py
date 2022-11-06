'''
Задание 5. Написать программу получающую набор
произведений чисел от 1 до N.
'''


def main():
    print("Введите натуральное число N")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        output_list = []
        output_list.extend(1 if n == 1 else n * output_list[n - 2] for n in range(1, int_target_number + 1))

        print(output_list)
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
