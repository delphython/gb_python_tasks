"""
Задание 2. Создать телефонный справочник с возможностью
импорта и экспорта данных в нескольких форматах.
"""

import csv
import json
import os
import sys


def show_phonebook():
    phonebook_file_path = "phonebook.csv"

    with open(phonebook_file_path, encoding = "UTF8") as csvfile:
        phonebook_items = csv.reader(csvfile, delimiter=";")

        for phonebook_item in phonebook_items:
            print("\t".join(phonebook_item))
        
    print("\n")


def import_from_cvs():
    phonebook_file_path = "phonebook.csv"
    phonebook_csv_file = "import_phonebook.csv"
    
    with open(phonebook_csv_file, "r", encoding="utf-8") as csvfile: 
        phonebook_items = csv.reader(csvfile, delimiter=";")

        with open(phonebook_file_path, "a", encoding="utf-8", newline="") as csvfile: 
            csv_writer = csv.writer(csvfile, delimiter=";", lineterminator=os.linesep)
        
            for phonebook_item in phonebook_items:
                csv_writer.writerow(phonebook_item)
    
    print("Все записи импортированы в справочник \n")


def import_from_json():
    phonebook_file_path = "phonebook.csv"
    phonebook_json_file = "import_phonebook.json"
    
    with open(phonebook_json_file, "r", encoding="utf-8") as jsonfile: 
        phonebook_items = json.load(jsonfile)

    with open(phonebook_file_path, "a", encoding="utf-8", newline="") as csvfile: 
        csv_writer = csv.writer(csvfile, delimiter=";", lineterminator=os.linesep)
    
        for phonebook_item in phonebook_items:
            csv_writer.writerow(phonebook_item.values())
    
    print("Все записи импортированы в справочник \n")


def export_to_cvs():
    phonebook_file_path = "phonebook.csv"
    phonebook_csv_file = "export_phonebook.csv"

    with open(phonebook_file_path, encoding="utf-8") as csvfile: 
        phonebook_items = csv.reader(csvfile, delimiter=";")

        with open(phonebook_csv_file, "w", encoding="utf-8", newline="") as csvfile: 
            csv_writer = csv.writer(csvfile, delimiter=";", lineterminator=os.linesep)

            for phonebook_item in phonebook_items:
                csv_writer.writerow(phonebook_item)
    
    print(f"Все записи экспортированы в cvs файл {phonebook_csv_file}\n")


def export_to_json():
    phonebook_file_path = "phonebook.csv"
    phonebook_json_file = "export_phonebook.json"
    phonebook_json_items = []

    with open(phonebook_file_path, encoding="utf-8") as csvfile: 
        phonebook_items = csv.DictReader(csvfile, delimiter=";")

        for phonebook_item in phonebook_items: 
            phonebook_json_items.append(phonebook_item)
    
    with open(phonebook_json_file, "w", encoding="utf-8") as jsonfile: 
        jsonfile.write(json.dumps(phonebook_json_items, indent=4))
    
    print(f"Все записи экспортированы в json файл {phonebook_json_file}\n")


def exit_from_script():
    sys.exit()


def main():
    operations = {
        "1": ("Показать все записи в справочнике", show_phonebook),
        "2": ("Импорт данных из файла (cvs) в справочник", import_from_cvs), 
        "3": ("Импорт данных из файла (json) в справочник", import_from_json), 
        "4": ("Экспорт данных из справочника в файл (cvs)", export_to_cvs),
        "5": ("Экспорт данных из справочника в файл (json)", export_to_json),
        "6": ("Выход", exit_from_script),
    }
    
    print("Телефонный справочник")
    while True:
        for number, operation in operations.items():
            print(f"{number} - {operation[0]}")
        print("Выберите номер операции:")
        selected_operation = input()
        selected_operation_value = operations.get(selected_operation)
        if selected_operation_value:
            selected_operation_value[1]()
        else:
            print("Выбрана неверная операция")


if __name__ == "__main__":
    main()
