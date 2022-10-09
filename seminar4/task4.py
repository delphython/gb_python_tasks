'''
Задание 4. Вычислить число c заданной точностью d
'''


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    pi = 3.1415926535897932384626433832795
    
    print("Введите заданную точность d")
    accuracy = input()

    if (is_float(accuracy) and
        float(accuracy) <= 1e-1 and
        float(accuracy) >= 1e-10):
        frac_part_count = len(accuracy.split('.')[1])
        print(f'{pi:.{frac_part_count}f}')
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
