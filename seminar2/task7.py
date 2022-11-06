'''
Задание 7. Задать список из N элементов, заполненных числами
из [-N, N]. Найти произведение элементов на указанных позициях.
Позиции хранятся в списке positions - создайте этот список 
(например: positions = [1, 3, 6]).
'''


import math


def main():
    positions = [1, 3, 6]


    target_number = 10
    target_list = list(range(-target_number, target_number + 1))


    needed_list = [
        x for index, x in enumerate(target_list) if index in positions
    ]

    print(f"Произведение элементов = {math.prod(needed_list)}")

if __name__ == "__main__":
    main()
