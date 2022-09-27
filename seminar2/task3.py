'''
Задание 3. Напишите программу, в которой пользователь будет
задавать две строки, а программа - определять количество
вхождений одной строки в другой.
'''


def get_input_values():
    print("Введите первую строку")
    first_string = input()

    print("Введите вторую строку")
    second_string = input()

    return first_string, second_string


def main():
    first_string, second_string = get_input_values()

    print(
        f"""Количество вхождений первой строки во вторую = 
        {second_string.count(first_string)}"""
    )


if __name__ == "__main__":
    main()
