'''
Задание 6. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между
максимальным и минимальным значением дробной части
элементов.
'''


def main():
    input_list = [1.1, 1.2, 3.1, 5, 10.01]

    fractional_part_list = [x % 1 for x in input_list]
    
    print(
        f"""Разница: 
        {max(fractional_part_list) - min(fractional_part_list)}
        """
    )

if __name__ == "__main__":
    main()
