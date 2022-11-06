'''
Задание 6. Задать список из n чисел последовательности
и вывести на экран их сумму.
'''


def main():
    print("Введите натуральное число n")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        output_list = [(1 + 1 / n) ** n for n in range(1, int_target_number+1)]
        print(
            f"""Сумма элементов последовательности =
            {sum(output_list)}"""
        )
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
