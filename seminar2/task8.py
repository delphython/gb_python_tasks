'''
Задание 8. Реализовать алгоритм перемешивания списка.
'''


import random


def mix_list(input_list):
    output_list = input_list[:]
    
    list_lenght = len(input_list)

    for i in range(list_lenght):
        randome_index = random.randint(0, list_lenght - 1)
        tmp = output_list[i]
        output_list[i] = output_list[randome_index]
        output_list[randome_index] = tmp
    
    return output_list


def main():
    initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        
    # hard way
    print(
        f"""Перемешанный спиcок сложным способом:
        {mix_list(initial_list)}"""
    )

    # easy way
    random.shuffle(initial_list)
    print(
        f"Перемешанный спиcок простым способом: {initial_list}"
    )

if __name__ == "__main__":
    main()
