'''
Задание 8. Сообщить в какой четверти координатной плоскости 
или на какой оси находится точка с координатами Х и У.
'''


def get_input_values():
    print("Введите координату X")
    coord_x = input()
    
    print("Введите координату Y")
    coord_y = input()

    return coord_x, coord_y


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    output_str = "Введены неверные значения координат"
    input_values = get_input_values()

    if all(is_int(input_value) for input_value in input_values):
        coord_x, coord_y = input_values
        int_coord_x = int(coord_x)
        int_coord_y = int(coord_y)

        if (int_coord_x != 0 and int_coord_y != 0):
            tmp_str = (
                "в первой четверти" if (int_coord_x > 0 and int_coord_y > 0) 
                else (
                    "во второй четверти" if (int_coord_x < 0 and int_coord_y > 0) 
                    else (
                        "в третьей четверти" if (int_coord_x < 0 and int_coord_y < 0)
                        else "в четвертой четверти"
                    ) 
                )
            )
        else:
            tmp_str = (
                "на оси Y" if (int_coord_x == 0 and int_coord_y != 0)  
                else (
                    "на оси X" if (int_coord_x != 0 and int_coord_y == 0) 
                    else "в нулевой точке"
                    ) 
            )

        output_str = (f"Коордиината ({coord_x}, {coord_y}) находится {tmp_str}")
    print(output_str)


if __name__ == "__main__":
    main()
