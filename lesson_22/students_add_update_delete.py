import json
from datetime import date
from sqlalchemy.orm import sessionmaker
from random import choice, sample
from sqlalchemy import extract

from lesson_22.alchemy_base import engine, Base
from lesson_22.tables.students_table import StudentsTable
from lesson_22.tables.courses_table import CoursesTable

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# add many students:
students = [
    StudentsTable(first_name='John', last_name='Smith', birth_date=date(2006, 5, 15)),
    StudentsTable(first_name='Jane', last_name='Doe', birth_date=date(2007, 8, 20)),
    StudentsTable(first_name='Alice', last_name='Johnson', birth_date=date(2005, 12, 1)),
    StudentsTable(first_name='Bob', last_name='Brown', birth_date=date(2006, 3, 30)),
    StudentsTable(first_name='Julian', last_name='Swinger', birth_date=date(2007, 4, 26)),
    StudentsTable(first_name='John', last_name='Baker', birth_date=date(2006, 3, 13)),
    StudentsTable(first_name='Emily', last_name='Clark', birth_date=date(2007, 7, 11)),
    StudentsTable(first_name='Michael', last_name='Scott', birth_date=date(2005, 11, 23)),
    StudentsTable(first_name='Sarah', last_name='Connor', birth_date=date(2006, 9, 17)),
    StudentsTable(first_name='David', last_name='Jones', birth_date=date(2007, 1, 25))
]
session.add_all(students)
session.commit()

# add new student:
new_student = StudentsTable(first_name='Johanna', last_name='Solemn',
                        birth_date=date(2007, 1, 7))
session.add(new_student)
session.commit()

# connect students to courses:
courses = session.query(CoursesTable).all()
for student in students:
    # random choice of course (<=2):
    selected_courses = sample(courses, k=choice([1, 2]))
    for course in selected_courses:
        student.courses.append(course)
session.commit()

# connect new student to course:
selected_courses_johanna = sample(courses, k=choice([1, 2]))
for course in selected_courses_johanna:
    new_student.courses.append(course)
session.commit()

# get course id, course name for student_id:
courses_for_student = CoursesTable.get_courses_by_student(session, student_id=2)
for course in courses_for_student:
    print(course)

# update specific student:
student_update = session.query(StudentsTable).filter_by(first_name='John', last_name='Smith').first()
if student_update:
    old_birth_date = student_update.birth_date
    student_update.birth_date = date(2005, old_birth_date.month, old_birth_date.day)
else:
    print("Student not found")

# update student selected by filters year=2005:
students_2005 = session.query(StudentsTable).filter(extract('year', StudentsTable.birth_date) == 2005).all()
for student_ in students_2005:
    old_birth_date = student_.birth_date
    student_.birth_date = date(year=2006, month=old_birth_date.month, day=old_birth_date.day)
session.commit()

# delete all students with first_name='John':
# for student in session.query(StudentsTable).filter_by(first_name='John').all():
#     session.delete(student)
# session.commit()

# delete all students:
# for student in session.query(StudentsTable).all():
#     session.delete(student)
# session.commit()

# select all students:
all_students = session.query(StudentsTable).all()
all_students_tuples = [(student.id, student.first_name, student.last_name, student.birth_date.isoformat())
                       for student in all_students]
print(all_students_tuples)

# all_students_dicts = [student.to_dict() for student in all_students]
# print(all_students_dicts)
# all_students_json = json.dumps(all_students_dicts, indent=4)
# print(all_students_json)


# SELECT * FROM students WHERE name = 'John' with first id_asc LIMIT 1:
john_first = session.query(StudentsTable).filter_by(first_name='John').order_by(StudentsTable.id.asc()).first()
print(john_first.id, john_first.first_name, john_first.last_name, john_first.birth_date)

# SELECT * FROM students ORDER BY id DESC(ASC)
# sorted_students = session.query(StudentsTable).order_by(StudentsTable.id.desc()).all()
sorted_students = session.query(StudentsTable).order_by(StudentsTable.id.asc()).all()
sorted_students_tuples = [(student.id, student.first_name, student.last_name, student.birth_date.isoformat())
                          for student in sorted_students]
print(sorted_students_tuples)
