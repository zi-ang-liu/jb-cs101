import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create tables
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Students (
    student_id TEXT PRIMARY KEY,
    name TEXT NOT NULL
)
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Courses (
    course_id TEXT PRIMARY KEY,
    course_name TEXT NOT NULL
)
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Enrollments (
    student_id TEXT,
    course_id TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)
"""
)


# Sample data
def insert_sample_data():
    cursor.execute(
        """
    INSERT INTO Students (student_id, name) VALUES
    ('S001', 'Alice'),
    ('S002', 'Bob'),
    ('S003', 'Charlie')
    """
    )
    cursor.execute(
        """
    INSERT INTO Courses (course_id, course_name) VALUES
    ('CS101', 'Computer Science'),
    ('CS102', 'Data Structures'),
    ('CS103', 'Algorithms')
    """
    )
    conn.commit()


# View functions
def list_students():
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)


def list_courses():
    cursor.execute("SELECT * FROM Courses")
    for row in cursor.fetchall():
        print(row)


def enroll_student(student_id, course_id):
    try:
        cursor.execute(
            "INSERT INTO Enrollments ('student_id', 'course_id') VALUES (?, ?)",
            (student_id, course_id),
        )
        conn.commit()
        print("Enrollment successful.")
    except sqlite3.IntegrityError:
        print("Enrollment failed. Check IDs or duplicate entry.")


def show_enrollments():
    cursor.execute(
        """
    SELECT Students.name, Courses.course_name
    FROM Enrollments
    JOIN Students ON Enrollments.student_id = Students.student_id
    JOIN Courses ON Enrollments.course_id = Courses.course_id
    """
    )
    for row in cursor.fetchall():
        print(f"{row[0]} is enrolled in {row[1]}")


# If the tables are empty, insert sample data
cursor.execute("SELECT COUNT(*) FROM Students")
if cursor.fetchone()[0] == 0:
    cursor.execute("SELECT COUNT(*) FROM Courses")
    if cursor.fetchone()[0] == 0:
        # Insert sample data if both tables are empty
        print("Inserting sample data...")
        insert_sample_data()


# Simple CLI
def menu():
    print(
        "\n1. List Students\n2. List Courses\n3. Enroll Student\n4. Show Enrollments\n5. Exit\n6. Show Options"
    )
    while True:
        choice = input("\nEnter choice: ")
        if choice == "1":
            list_students()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            s_id = input("Student ID: ")
            c_id = input("Course ID: ")
            enroll_student(s_id, c_id)
        elif choice == "4":
            show_enrollments()
        elif choice == "5":
            break
        elif choice == "6":
            print(
                "\n1. List Students\n2. List Courses\n3. Enroll Student\n4. Show Enrollments\n5. Exit\n6. Show Options\n"
            )
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
    conn.close()
