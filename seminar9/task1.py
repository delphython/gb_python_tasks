'''
Задание 1. Задайте строку из набора чисел. Напишите программу,
которая покажет большее и меньшее число. В качестве 
символа-разделителя используйте пробел.

Добавить тесты
'''


def test_all_numbers():
    input_str = "1 234 556 7 8 O 9"
    res = get_list_from_str(input_str)
    assert all(x.isDigit for x in res)


def get_list_from_str(input_str):
    return list(map(int, input_str.split(" ")))


def main():
    input_str = "1 234 556 7 8 0 9"

    number_list = get_list_from_str(input_str)
    
    print(
        f"""Минимальное число: {min(number_list)}
        Максимальное число {max(number_list)}
        """
    )

if __name__ == "__main__":
    main()
