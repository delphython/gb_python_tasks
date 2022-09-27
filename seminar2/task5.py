'''
Задание 5. Написать программу получающую набор
произведений чисел от 1 до N.
'''


def main():
    output_list = []
    print("Введите натуральное число N")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        for n in range(1, int_target_number+1):
            output_list.append(
                1 if n == 1 else n * output_list[n-2]
            )
        print(output_list)
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
