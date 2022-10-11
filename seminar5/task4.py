'''
Задание 4. Создайте программу для игры с
конфетами человек против человека.
'''

import random


def create_two_players_game(candies_count, max_candies_to_get):
    player = random.randint(1, 2)
    
    print(
        f"Жеребьевкой выбран для первого хода игрок №{player}"
    )

    while candies_count > 0:
        print(f"Осталось {candies_count} конфет")
        print(f"Игрок {player}, Ваш ход")
        print(
            f"""
            За один ход можно забрать не более 
            чем {max_candies_to_get} конфет или не более, чем осталось
            """
        )
        next_move = input()
        while (
            not next_move.isdigit() or
            int(next_move) > max_candies_to_get or 
            int(next_move) > candies_count
        ):
            print("Введено некорректное число конфет, повторите ввод")
            next_move = input()
        candies_count -= int(next_move)
        
        if candies_count > 0:
            player = 3 - player
    
    print(f"Выиграл игрок {player}")


def get_best_number(candies_count, max_candies_to_get):
    if (candies_count // max_candies_to_get > 2 or
        candies_count - 1 == max_candies_to_get):
        return max_candies_to_get
    elif candies_count // max_candies_to_get == 2:
        return max_candies_to_get - 1    
    elif candies_count <= max_candies_to_get:
        return candies_count
    else:
        return candies_count - max_candies_to_get - 1


def create_bot_game(candies_count, max_candies_to_get, is_bot_smart="False"):
    player = random.randint(1, 2)

    player_name = "человек" if player == 1 else "бот"
            
    print(
        f"Жеребьевкой выбран для первого хода игрок {player_name}"
    )

    while candies_count > 0:
        player_name = "человек" if player == 1 else "бот"

        print(f"Осталось {candies_count} конфет")
        print(f"Игрок {player_name}, Ваш ход")
        print(
            f"""
            За один ход можно забрать не более 
            чем {max_candies_to_get} конфет или не более, чем осталось
            """
        )
        if player == 1:
            next_move = input()
            while (
                not next_move.isdigit() or
                int(next_move) > max_candies_to_get or 
                int(next_move) > candies_count
            ):
                print("Введено некорректное число конфет, повторите ввод")
                next_move = input()
            candies_count -= int(next_move)
        else:
            if is_bot_smart:
                bot_next_move = get_best_number(
                    candies_count, max_candies_to_get
                )
            else:
                max_candies_count = (
                    max_candies_to_get 
                    if candies_count >= max_candies_to_get
                    else candies_count
                )
                bot_next_move = random.randint(1, max_candies_count)
            print(f"Бот выбрал количество конфет {bot_next_move}")
            candies_count -= bot_next_move

        if candies_count > 0:
            player = 3 - player
        
    print(f"Выиграл игрок {player_name}")


def main():
    candies_count = 121
    max_candies_to_get = 28

    print(
        f"""
        Игра с конфетами! На столе лежит 2021 конфета. 
        Играют два игрока делая ход друг после друга. 
        Первый ход определяется жеребьёвкой. За один ход
        можно забрать не более чем {max_candies_to_get} конфет.
        Все конфеты оппонента достаются сделавшему последний ход.
        """
    )
    print(
        """
        Введите 1, если игра с оппонентом
        Введите 2, если игра с ботом
        Введите любой другой символ для выхода
        """
    )
    input_choice = input()
    if input_choice == "1":
        print("Выбрана игра с оппонентом")
        create_two_players_game(candies_count)
    elif input_choice == "2":
        print("Выбрана игра с ботом")
        create_bot_game(candies_count, max_candies_to_get, True)
    else:
        print("Выход из игры")


if __name__ == "__main__":
    main()
