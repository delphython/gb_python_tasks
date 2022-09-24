'''
Задание 3. Вывести на экран числа от -N до N.
'''


def main():
    print("Введите число N")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        for output_number in range(-int_target_number, int_target_number+1):
            print(output_number)
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
