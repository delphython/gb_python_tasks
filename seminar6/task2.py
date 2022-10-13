'''
Задание 2. Дана строка. Необходимо получить словарь,
в котором ключи – слова, значения – количество слов
в строке:
'''


def main():
    input_str = "дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул"

    word_list = list(input_str.split(", "))

    word_dict = {word:word_list.count(word) for word in word_list}
    
    print(word_dict)

if __name__ == "__main__":
    main()
