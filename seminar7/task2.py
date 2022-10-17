"""
Задание 2. Создать телефонный справочник с возможностью
импорта и экспорта данных в нескольких форматах.
"""

import sys


def add_to_phonebook():
    pass


def show_phonebook():
    pass


def import_from_cvs():
    pass


def import_from_json():
    pass


def export_to_cvs():
    pass


def export_to_json():
    pass


def exit_from_script():
    sys.exit()



def main():
    operations = {
        "1": ("Добавить запись в справочник", add_to_phonebook),
        "2": ("Показать все записи в справочнике", show_phonebook),
        "3": ("Импорт данных из файла (cvs) в справочник", import_from_cvs), 
        "4": ("Импорт данных из файла (json) в справочник", import_from_json), 
        "5": ("Экспорт данных из справочника в файл (cvs)", export_to_cvs),
        "6": ("Экспорт данных из справочника в файл (json)", export_to_json),
        "7": ("Выход", exit_from_script),
    }
    
    print("Телефонный справочник")
    while True:
        for number, operation in operations.items():
            print(f"{number} - {operation[0]}")
        print("Выберите номер операции:")
        selected_operation = input()
        operations[selected_operation][1]()


if __name__ == "__main__":
    main()
