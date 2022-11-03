import sqlite3


def create_tables(cursor):
    cursor.execute(
        """
        create table if not exist students (
            student_id integer primary key autoincrement,
            first_name varchar(255) not null,
            last_name varchar(255) not null,
            training_course integer not null,
            group_number varchar(10) not null,
        )
        """
    )

    cursor.execute(
        """
        create table if not exist grades (
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


def main():
    bd_tables = {
        "students": "студенты",
        "grades": "оценки",
    }

    conn = sqlite3.connect("test.db")

    cursor = conn.cursor()
    create_tables(cursor)


if __name__ == "__main__":
    main()