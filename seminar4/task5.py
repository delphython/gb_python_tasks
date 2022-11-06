'''
Задание 5. Задайте натуральное число N.
Напишите программу, которая составит 
список простых множителей числа N.
'''


def get_factorization(input_number):
    output_list = []
    d = 2

    while d**2 <= input_number:
        if input_number % d == 0:
            output_list.append(d)
            input_number //= d
        else:
            d += 1
    if input_number > 1:
        output_list.append(input_number)

    return output_list


def main():
    print("Введите число N")
    target_number = input()

    if target_number.isdigit():
        int_target_number = int(target_number)
        print(
            f"""Простые множители:
            {get_factorization(int_target_number)}"""
        )
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
