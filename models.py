from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    roll_no = Column(String, index=True, unique=True, nullable=False)
    phone_no = Column(Integer, index=True, unique=True, nullable=False)
    course = Column(String, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'roll_no': self.roll_no,
            'phone_no': self.phone_no,
            'course': self.course,
            'address': self.address,
        }

    def update(self, student):
        self.name = student.name
        self.email = student.email
        self.roll_no = student.roll_no
        self.phone_no = student.phone_no
        self.course = student.course
        self.address = student.address
