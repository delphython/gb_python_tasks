'''
Задание 2. Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число.
'''


def main():
    input_list = ["ksd", "lasland", 2.3]

    tmp_str = (
            "присутствует" if (
                any(
                    type(input_value) in {int, float} 
                    for input_value in input_list
                )
            ) else "не присутствует"
        )

    print(f"В заданном списке строк {tmp_str} некое число")

if __name__ == "__main__":
    main()
