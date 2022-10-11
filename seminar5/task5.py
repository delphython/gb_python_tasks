'''
Задание 5. Создайте программу для игры в "Крестики-нолики".
'''


def print_board(values):
    print(
        f"""
             |     |     
          {values[0]}  |  {values[1]}  |  {values[2]}  
        _____|_____|_____
             |     |     
          {values[3]}  |  {values[4]}  |  {values[5]}  
        _____|_____|_____
             |     |     
          {values[6]}  |  {values[7]}  |  {values[8]}  
             |     |    
        """
    )


def main():
    values = list(range(1, 10))
    print_board(values)


if __name__ == "__main__":
    main()
