'''
Задание 6. Реализуйте RLE алгоритм: реализуйте
модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных 
текстовых файлах.
'''


from itertools import groupby


def encode_str(text):
    encode = ""
    i = 0
 
    while i < len(text):
        count = 1
 
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
 
        encode += str(count) + text[i]
        i += 1
 
    return encode


def decode_str(text):
    decode = ''
    count = ''
    
    for char in text:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    
    return decode


def main():
    file_in = "task6_in.txt"
    file_out = "task6_out.txt"

    with open(file_in, "r") as f:
        text_to_encode = f.read()

    print(text_to_encode)
    encoded_text = encode_str(text_to_encode)
    print(encoded_text)

    with open(file_out, "w") as f:
        f.write(encoded_text)

    print(decode_str(encoded_text))


if __name__ == "__main__":
    main()
