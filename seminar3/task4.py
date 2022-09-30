'''
Задание 2. Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
'''


def main():
    input_list = [2, 3, 5, 9, 3]
   
    odd_list = [x for i, x in enumerate(input_list) if i%2 != 0]

    print(f"Сумма нечетных элементов списка: {sum(odd_list)}")

if __name__ == "__main__":
    main()
