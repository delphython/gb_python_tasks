'''
Задание 1. В файле находится N натуральных чисел,
записанных через пробел. Среди чисел не хватает
одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
Найдите это число.
'''


def find_number(input_list):
    for i in range(len(input_list)):
        if input_list[i+1] - 1 != input_list[i]:
            return input_list[i] + 1


def main():
    file_name = "file_task1.txt"
    
    with open(file_name, "r") as f:
        input_list = list(map(int, f.read().split(" ")))

    print(find_number(input_list))


if __name__ == "__main__":
    main()
