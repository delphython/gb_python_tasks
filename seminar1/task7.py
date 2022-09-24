'''
Задание 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
'''


def get_input_values():
    input_values = []
    for _ in range(3):
        print("Введите любой символ или строку")
        input_values.append(input())

    return input_values


def main():
    x, y, z = get_input_values()

    print((not (x or y or z)) == ((not x and not y and not z)))


if __name__ == "__main__":
    main()