'''
Задание 2. Напишите программу, которая найдёт произведение 
пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
'''


def main():
    input_list = [2, 3, 4, 5, 6]
    output_list = []

    input_list_len = len(input_list) - 1
   
    for i in range(input_list_len):
        if (input_list_len - 2 * i) >= 0:
            output_list.append(
                input_list[i] * input_list[input_list_len-i]
            )

    print(f"Произведения пар чисел: {output_list}")

if __name__ == "__main__":
    main()
