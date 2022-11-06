'''
Задание 2. Для натурального n создать список, состоящий
из элементов последовательности 3n + 1.
'''


def main():
    print("Введите натуральное число n")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        output_list = [3 * n + 1 for n in range(1, int_target_number+1)]
        print(output_list)
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
