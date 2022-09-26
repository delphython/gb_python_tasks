'''
Задание 10. Найти расстояние между двумя точками пространства.
'''


def get_input_values():
    print("Введите координату X первой точки")
    first_coord_x = input()
    
    print("Введите координату Y первой точки")
    first_coord_y = input()

    print("Введите координату X второй точки")
    second_coord_x = input()

    print("Введите координату Y второй точки")
    second_coord_y = input()

    return first_coord_x, first_coord_y, second_coord_x, second_coord_y


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_distance_between_points(points_coords):
    first_coord_x, first_coord_y, second_coord_x, second_coord_y = points_coords

    return round(
        (
            (
                (int(second_coord_x) - int(first_coord_x)) ** 2 +
                (int(second_coord_y) - int(first_coord_y)) ** 2
            ) ** 0.5
        ), 2
    )


def main():
    output_str = "Введены неверные значения чисел"
    input_values = get_input_values()

    if all(is_int(input_value) for input_value in input_values):
        output_str = (
            f"Расстояние между двумя точками = {get_distance_between_points(input_values)}"
        )

    print(output_str)


if __name__ == "__main__":
    main()
