from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from lesson_22.alchemy_base import Base
from lesson_22.tables.student_course_table import student_course_table

class StudentsTable(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True) # unique and not none
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date, nullable=False)

    courses = relationship('CoursesTable', secondary=student_course_table, back_populates='students')

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat()
        }

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name})>"

    @classmethod
    def get_students_by_course(cls, session, course_id):
        from lesson_22.tables.courses_table import CoursesTable
        return session.query(cls).join(cls.courses).filter(CoursesTable.id == course_id).all()

    @classmethod
    def get_courses_by_student(cls, session, student_id):
        student = session.query(cls).get(student_id)
        return student.courses if student else []