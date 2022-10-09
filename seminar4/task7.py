'''
Задание 7. Задана натуральная степень k. Сформировать случайным
образом список коэффициентов (значения от 0 до 100) многочлена и
записать в файл многочлен степени k.
'''


import random


def main():
    print("Введите степень многочлена")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)

        tmp_list = []
        for i in range(int_target_number, -1, -1):
            koeff_rand = random.randint(0, 100)
            if koeff_rand != 0:
                polynomial_member = (
                    f"{koeff_rand}x^{i}" if i > 1 else (
                        f"{koeff_rand}x" if i == 1 else f"{koeff_rand}"
                    )
                )
                tmp_list.append(polynomial_member)

        file_name = "file1.txt"

        with open(file_name, "w") as file:
            file.write(f"{' + '.join(tmp_list)} = 0") 

    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
