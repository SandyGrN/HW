# Practice

# 1. Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
# 2. Find all students` name that visited 'English' classes 

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student_Subject(Base):
    __tablename__ = 'student_subject' 

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('student.id'))
    subject_id = Column(ForeignKey('subject.id'))
    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")
    
    def __str__(self):
        return f'Student {self.student.name} visited {self.subject.name} classes.'
    
    def __repr__(self):
        return f'Student {self.student.name} visited {self.subject.name} classes.'

class Student(Base):
    __tablename__ = 'student' 

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    subjects = relationship("Student_Subject", back_populates="student")
    
    def __str__(self):
        return f'This is a student {self.name}. Age: {self.age}'
    
    def __repr__(self):
        return f'This is a student {self.name}. Age: {self.age}'



class Subject(Base):
    __tablename__ = 'subject' 

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student_Subject", back_populates="subject")
    
    def __str__(self):
        return f'This is a subject {self.name}. Id: {self.id}'
    
    def __repr__(self):
        return f'This is a subject {self.name}. Id: {self.id}'


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='oleksandra',
        password='',
        port=5432,
    )
)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


first_student = session.query(Student).first()
print(first_student)


first_subject = session.query(Subject).first()
print(first_subject)


first_row = session.query(Student_Subject).first()
print(first_row)



english_students =  session.query(Student_Subject).join(Student, Subject).filter(Subject.name=='English').all()
print(english_students)
