'''
Задание 6. Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной 
последовательности.
'''


def main():
    input_list = [2, 3, 5, 9, 3]

    output_list = [i for i in input_list if input_list.count(i) == 1]
   
    print(output_list)

if __name__ == "__main__":
    main()
