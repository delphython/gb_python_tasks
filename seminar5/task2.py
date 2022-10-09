'''
Задание 2. Дан список чисел. Создайте список,
в который попадают числа, описываемые возрастающую
последовательность. Порядок элементов менять нельзя.
'''


def main():
    input_list = [1, 5, 2, 3, 4, 6, 1, 7]

    for i in range(len(input_list)-1):
        if (input_list[i + 1] > input_list[i]) and ():
            output_list.append(input_list[i])


    output_list = [input_list[i] for i in range(len(input_list)-1) if (input_list[i + 1] > input_list[i])]

    print(output_list)

if __name__ == "__main__":
    main()
