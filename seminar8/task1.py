import sqlite3

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


def get_items_from_bd(cursor):
    rows = cursor.execute(
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

    return pd.DataFrame(
        rows,
        columns = [
            'Имя',
            'Фамилия',
            '№ курса',
            '№ группы',
            "Предмет",
            "Оценка",
            "Дата"
        ]
        )


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

    print(get_items_from_bd(cursor))

if __name__ == "__main__":
    main()