'''
Задание 8. Задана натуральная степень k. Сформировать случайным
образом список коэффициентов (значения от 0 до 100) многочлена и
записать в файл многочлен степени k.
'''


def main():
    tmp_list = []
    file_name = "file.txt"
    files = ["file1.txt", "file2.txt"]

    for file in files:
        with open(file, "r") as f:
            tmp_list += f.read().split(" = ")[0].split(" + ")
    
    target_list = list(
        map(int, [x.split("x")[0] for x in tmp_list])
    )
                
    with open(file_name, "w") as file:
        file.write(f"{sum(target_list)}") 


if __name__ == "__main__":
    main()
