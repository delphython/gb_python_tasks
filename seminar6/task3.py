'''
Задание 3. Дан файл. Необходимо получить словарь,
в котором ключи – слова, значения – количество слов
в файле:
'''


def main():
    file_in = "jack.txt"
    with open(file_in, "r", encoding="UTF8") as f:
        text_to_parse = f.read()

    word_list = list(text_to_parse.split())

    ch = lambda x: x.replace(',', '').replace('.', '')

    word_list_ch = list(map(ch, word_list))

    word_dict = {word:word_list_ch.count(word) for word in word_list_ch}
    
    print(word_dict)

if __name__ == "__main__":
    main()
