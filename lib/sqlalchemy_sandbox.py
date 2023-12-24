# lib/sqlalchemy_sandbox.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    # Create a session
    session = Session()

    try:
        # Update the existing student's name to "Geoffrey Nyanyuki"
        existing_student = session.query(Student).filter_by(id=1).first()
        if existing_student:
            existing_student.name = 'Geoffrey Nyanyuki'
            session.commit()

        # Query all students
        all_students = session.query(Student).all()
        for student in all_students:
            print(f"Student ID: {student.id}, Name: {student.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the session
        session.close()
