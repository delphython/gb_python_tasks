import sqlite3
import sys

import pandas as pd


def create_tables(cursor):
    cursor.execute(
        """
        create table if not exists students (
            student_id integer primary key autoincrement,
            first_name varchar(255) not null,
            last_name varchar(255) not null,
            training_course integer not null,
            group_number varchar(10) not null
        )
        """
    )

    cursor.execute(
        """
        create table if not exists grades (
            grade_id integer primary key autoincrement,
            student_id integer not null,
            subject varchar(255),
            grade integer not null,
            grade_date date not null,
            FOREIGN KEY (student_id)
                REFERENCES students (student_id) 
        )
        """
    )


def insert_test_data(
    cursor,
    students_test_items,
    grades_test_items
):
    cursor.executemany(
        """
        insert or replace into students (
            first_name,
            last_name,
            training_course,
            group_number
        ) values (?, ?, ?, ?)
        """,
        students_test_items
    )
    cursor.executemany(
        """
        insert or replace into grades (
            student_id,
            subject,
            grade,
            grade_date
        ) values (?, ?, ?, ?)
        """,
        grades_test_items
    )


def get_items_from_bd(*args):
    rows = args[0][0].execute(
        """
        SELECT 
        students.first_name,
        students.last_name,
        students.training_course,
        students.group_number,
        grades.subject,
        grades.grade,
        grades.grade_date
        from students
        inner join grades on students.student_id = grades.student_id
        """
    ).fetchall()

    print(pd.DataFrame(
        rows,
        columns = [
            "Имя",
            "Фамилия",
            "№ курса",
            "№ группы",
            "Предмет",
            "Оценка",
            "Дата"
        ]
        )
    )


def get_items_from_table(*args):
    cursor, table_name = args[0]
    if table_name == "students":
        rows = cursor.execute(
            """
            SELECT
            student_id, 
            first_name,
            last_name,
            training_course,
            group_number
            from students
            order by first_name,
            last_name
            """
        ).fetchall()

        print(pd.DataFrame(
            rows,
            columns = [
                "id",
                "Имя",
                "Фамилия",
                "№ курса",
                "№ группы",
            ]
            )
        )
    elif table_name == "grades":
        rows = cursor.execute(
            """
            SELECT
            grade_id,
            student_id, 
            subject,
            grade,
            grade_date
            from grades
            order by subject,
            grade_date
            """
        ).fetchall()

        print(pd.DataFrame(
            rows,
            columns = [
                "id",
                "student id",
                "Предмет",
                "Оценка",
                "Дата",
            ]
            )
        )


def insert_item_to_table(*args):
    cursor, table_name = args[0]
    if table_name == "students":
        students_data = []
        students_fields = [
            "Имя",
            "Фамилия",
            "№ курса",
            "№ группы"
        ]
        print(f"Введите данные полей таблицы {table_name}:")        
        for students_field in students_fields:
            students_data.append(
                input(f"Данные поля {students_field}:")
            )
        print(students_data)
        cursor.execute(
        """
        insert or replace into students (
            first_name,
            last_name,
            training_course,
            group_number
        ) values (?, ?, ?, ?)
        """,
        (students_data)
    )
    elif table_name == "grades":
        grades_data = []
        grades_fields = [
            "student id",
            "Предмет",
            "Оценка",
            "Дата"
        ]
        print(f"Введите данные полей таблицы {table_name}:")        
        for grades_field in grades_fields:
            grades_data.append(
                input(f"Данные поля {grades_field}:")
            )
        cursor.execute(
            """
            insert or replace into grades (
                student_id,
                subject,
                grade,
                grade_date
            ) values (?, ?, ?, ?)
            """,
            (grades_data)
        )


def update_item_in_table(*args):
    cursor, table_name = args[0]
    id_to_update = input(
        f"Введите id таблицы {table_name} для изменения:"
    )
    if table_name == "students":
        students_data = []
        students_fields = [
            "Имя",
            "Фамилия",
            "№ курса",
            "№ группы"
        ]
        print(f"Введите данные полей таблицы {table_name}:")        
        for students_field in students_fields:
            students_data.append(
                input(f"Данные поля {students_field}:")
            )
        students_data.append(id_to_update)
        cursor.execute(
        """
        update students set 
            first_name = ?,
            last_name = ?,
            training_course = ?,
            group_number = ?
        where student_id = ?
        """,
        (students_data)
    )
    elif table_name == "grades":
        grades_data = []
        grades_fields = [
            "student id",
            "Предмет",
            "Оценка",
            "Дата"
        ]
        print(f"Введите данные полей таблицы {table_name}:")        
        for grades_field in grades_fields:
            grades_data.append(
                input(f"Данные поля {grades_field}:")
            )
        grades_data.append(id_to_update)
        cursor.execute(
            """
            update grades set
                student_id = ?,
                subject = ?,
                grade = ?,
                grade_date = ?
            where grade_id = ?
            """,
            (grades_data)
        )


def delete_item_from_table(*args):
    cursor, table_name = args[0]
    id_to_delete = input(f"Введите id таблицы {table_name} для удаления:")
    if table_name == "students":
        cursor.execute(
            """
            delete from students where
            student_id = ?
            """,
            id_to_delete
        )
    elif table_name == "grades":
        cursor.execute(
            """
            delete from grades where
            grade_id = ?
            """,
            id_to_delete
        )


def exit_from_script(*args):
    sys.exit()


def main():
    students_test_items = [
        ("Иван", "Иванов", 2, "45А"),
        ("Петр", "Петров", 2, "15Б"),
    ]

    grades_test_items = [
        (1, "Математика", 5, "01.11.2022"),
        (2, "История", 2, "02.11.2022"),
    ]

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    create_tables(cursor)

    insert_test_data(
        cursor,
        students_test_items,
        grades_test_items
    )

    operations = {
        "1": (
            "Показать все записи в базе",
            get_items_from_bd,
            [cursor]),
        "2": (
            "Показать все записи таблицы students",
            get_items_from_table,
            [cursor, "students"]), 
        "3": (
            "Показать все записи таблицы grades",
            get_items_from_table,
            [cursor, "grades"]),
        "4": (
            "Добавить запись в таблицу students",
            insert_item_to_table,
            [cursor, "students"]), 
        "5": (
            "Добавить запись в таблицу grades",
            insert_item_to_table,
            [cursor, "grades"]),
        "6": (
            "Изменить запись в таблице students",
            update_item_in_table,
            [cursor, "students"]), 
        "7": (
            "Изменить запись в таблице grades",
            update_item_in_table,
            [cursor, "grades"]),
        "8": (
            "Удалить запись из таблицы students",
            delete_item_from_table,
            [cursor, "students"]),
        "9": (
            "Удалить запись из таблицы grades",
            delete_item_from_table,
            [cursor, "grades"]),
        "10": ("Выход", exit_from_script, []),
    }

    print("База данных для студентов")
    while True:
        for number, operation in operations.items():
            print(f"{number} - {operation[0]}")
        print("Выберите номер операции:")
        selected_operation = input()
        if selected_operation_value := operations.get(selected_operation):
            selected_operation_value[1](selected_operation_value[2])
        else:
            print("Выбрана неверная операция")


if __name__ == "__main__":
    main()
