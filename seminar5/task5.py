'''
Задание 5. Создайте программу для игры в "Крестики-нолики".
'''


def print_board(cells):
    print(
        f"""
             |     |     
          {cells[0]}  |  {cells[1]}  |  {cells[2]}  
        _____|_____|_____
             |     |     
          {cells[3]}  |  {cells[4]}  |  {cells[5]}  
        _____|_____|_____
             |     |     
          {cells[6]}  |  {cells[7]}  |  {cells[8]}  
             |     |    
        """
    )


def is_winner(cells, xo_item):
    winning_combinations = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

    xo_item_idx = [
        i for i, x in enumerate(cells) if x == xo_item
    ]

    return any(
        set(winning_combination).issubset(xo_item_idx) 
        for winning_combination in winning_combinations
    )


def make_move(cells, xo_item):
    print(f"Игрок {xo_item}, выберите номер ячейки")
    target_cell = input()

    while (
        not target_cell.isdigit() or
        int(target_cell) not in list(range(1, 10))
    ):
        print("Введен некорректный номер ячейки")
        target_cell = input()

    while int(target_cell) not in cells:
        print("Ячейка уже занята, введите другую")
        target_cell = input()
    
    cells[int(target_cell)-1] = xo_item
    
    return cells


def main():
    cells = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]

    xo_items = ("X", "0")

    is_exit = False

    while not is_exit:
        print_board(cells)
        for xo_item in xo_items:
            cells = make_move(cells, xo_item)
            print_board(cells)
            if is_winner(cells, xo_item):
                print(f"Победитель: {xo_item}")
                is_exit = True
                break
            if all(str(i) in xo_items for i in cells):
                print("Ничья")
                is_exit = True
                break


if __name__ == "__main__":
    main()
