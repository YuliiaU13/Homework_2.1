from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from lesson_22.alchemy_base import Base
from lesson_22.tables.student_course_table import student_course_table
from lesson_22.tables.students_table import StudentsTable


class CoursesTable(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    students = relationship('StudentsTable', secondary=student_course_table, back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name})>"

    @classmethod
    def get_courses_by_student(cls, session, student_id):
        return session.query(cls).join(cls.students).filter(StudentsTable.id == student_id).all()

    @classmethod
    def get_students_by_course(cls, session, course_id):
        course = session.query(cls).get(course_id)
        return course.students if course else []