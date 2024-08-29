from sqlalchemy.orm import sessionmaker

from lesson_22.alchemy_base import engine, Base
from lesson_22.tables.courses_table import CoursesTable
from lesson_22.tables.students_table import StudentsTable

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# add many courses:
# courses = [
#     CoursesTable(name='Math', description='Mathematics Course'),
#     CoursesTable(name='Science', description='Science Course'),
#     CoursesTable(name='History', description='History Course'),
#     CoursesTable(name='Art', description='Art Course'),
#     CoursesTable(name='Programming', description='Programming Course')
# ]
# session.add_all(courses)
# session.commit()

course_id = 1
students_in_math = StudentsTable.get_students_by_course(session, course_id)
for student in students_in_math:
    course_names = [course.name for course in student.courses]
    print(f"{student.first_name} {student.last_name}, student_id={student.id}, course names: {', '.join(course_names)}")

# update course by name:
course_to_update = session.query(CoursesTable).filter_by(name='Math').first()
if course_to_update:
    course_to_update.name = 'Advanced Math'
    course_to_update.description = 'Advanced Mathematics Course'
    session.commit()
    print(f"Course updated: {course_to_update.name}, {course_to_update.description}")
else:
    print("Course not found.")