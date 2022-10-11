'''
Задание 6. Реализуйте RLE алгоритм: реализуйте
модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных 
текстовых файлах.
'''


from itertools import groupby


def encode_str(text):
    return "".join([f"{c}{sum(1 for _ in g)}" for c, g in groupby(text)])


def decode_str(text):
    pass


def main():
    file_in = "task6_in.txt"
    file_out = "task6_out.txt"

    with open(file_in, "r") as f:
        input_text = f.read()

    print(encode_str(input_text))


if __name__ == "__main__":
    main()
