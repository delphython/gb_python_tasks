'''
Задание 2. Напишите программу, которая определит позицию
второго вхождения строки в списке либо сообщит, что её нет.
'''


def main():
    input_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    what_to_find = "qwes"

    index_list = [
        i for i, x in enumerate(input_list) if x == what_to_find
    ]

    second_entry = index_list[1] if len(index_list) >= 2 else -1


    print(f"Позиция второго вхождения строки в списко: {second_entry}")

if __name__ == "__main__":
    main()
