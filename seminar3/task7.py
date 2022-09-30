"""
Задание 7. Напишите программу, которая будет
преобразовывать десятичное число в двоичное.
"""


def convert_dec_to_bin(input_number):
    output_bin = ""
    
    while (input_number > 0):
        bin_digit = "0" if input_number % 2 == 0 else "1"
        output_bin += bin_digit
        input_number //= 2
    
    return output_bin[::-1]


def main():
    print("Введите число")
    target_number = input()

    if target_number.isdigit():
        print(
            f"""Десятичное число {target_number} преобразовано 
            в двоичное {convert_dec_to_bin(int(target_number))}"""
        )
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
