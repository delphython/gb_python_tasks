'''
Задание 2. Дан список чисел. Создайте список,
в который попадают числа, описываемые возрастающую
последовательность. Порядок элементов менять нельзя.
'''


def get_increasing_sequence(input_list):
    output_list = []
    tmp_list = []
    
    input_list_len = len(input_list)
    
    for i in range(input_list_len):
        if i < input_list_len - 1 and input_list[i] <= input_list[i+1]:
            tmp_list.append(input_list[i])
        else:
            tmp_list.append(input_list[i])
            if len(tmp_list) > 1:
                output_list.append(tmp_list)
            tmp_list = []
    
    return output_list


def main():
    input_list = [6, 5, 2, 7, 9, 6, 10, 2]
    output_list = get_increasing_sequence(input_list)

    print(output_list)


if __name__ == "__main__":
    main()
