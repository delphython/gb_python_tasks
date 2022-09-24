'''
Задание 6. Дано число обозначающее день недели. 
Вывести его название и указать является ли он выходным.
'''


def main():
    day_of_week = {
        1: "понедельник",
        2: "вторник",
        3: "среда",
        4: "четверг",
        5: "понедельник",
        6: "суббота",
        7: "воскресенье",
    }

    print("Введите число обозначающее день недели")
    target_number = input()

    if target_number.isdigit() & (int(target_number) in day_of_week):
        int_target_number = int(target_number)
        print(day_of_week[int_target_number])
        print("выходной" if int_target_number in {6, 7} else "не выходной")
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
