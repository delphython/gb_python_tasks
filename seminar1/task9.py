'''
Задание 9. Указав номер четверти прямоугольной системы координат,
показать допустимые значения координат для точек этой четверти.
'''


def main():
    print("Введите номер четверти")
    target_number = input()

    if target_number.isdigit() and target_number in {"1", "2", "3", "4"}:
        coord_quarters = {
            "1": "по оси X: [0, +∞), по оси Y: [0, +∞)",
            "2": "по оси X: [0, -∞), по оси Y: [0, +∞)",
            "3": "по оси X: [0, -∞), по оси Y: [0, +∞)",
            "4": "по оси X: [0, +∞), по оси Y: [0, -∞)",
        }
        print(
            f"""
            Допустимые значения координат для точек {target_number} четверти:
            {coord_quarters[target_number]}
            """
        )
    else:
        print("Введено неверное число")


if __name__ == "__main__":
    main()
