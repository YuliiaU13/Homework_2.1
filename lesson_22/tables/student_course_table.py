from sqlalchemy import Column, Integer, String, ForeignKey, Table
from lesson_22.alchemy_base import Base


student_course_table = Table(
    'student_course_table', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
