'''
Задание 1. Задайте строку из набора чисел. Напишите 
программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.
'''


def main():
    input_str = "23 45 6 7789 1 4 321 53474 2"

    number_list = input_str.split(" ") 
    
    print(
        f"""Разница: 
        {max(fractional_part_list) - min(fractional_part_list)}
        """
    )

if __name__ == "__main__":
    main()
