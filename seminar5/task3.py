'''
Задание 3. Напишите программу, удаляющую из
текста все слова, содержащие "абв".
'''


def main():
    input_str = "фыжваф абвгдейка фыдлаыва пабврррр фыдлводывао ыдлвоаыдва абвабвабв"
    target_str = "абв"
    
    input_list = input_str.split(" ")
    
    output_list = [
        text_word for text_word in input_list if target_str not in text_word
    ]

    print((" ").join(output_list))


if __name__ == "__main__":
    main()
