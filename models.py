from sqlalchemy import Column, Integer, String, Date
from database import Base
from datetime import datetime


class Employee(Base):
    """Employee model"""
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False, index=True)
    sex = Column(String, nullable=False, index=True)

    def __init__(self, name: str, date_of_birth: str, sex: str):

        if not name or len(name) > 255 or not isinstance(name, str):
            raise ValueError('Invalid name format')

        try:
            dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Invalid date format, expected YYYY-MM-DD')

        today = datetime.today()
        if dob >= today:
            raise ValueError('Date of birth cannot be in the future or today')

        if sex not in ('Male', 'Female'):
            raise ValueError('Invalid sex format')

        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        self.sex = sex

    def get_age(self) -> int:
        """Calculates age of an employee"""
        today = datetime.today().date()
        employee_age = today.year - self.date_of_birth.year - 1
        if (today.month, today.day) >= (self.date_of_birth.month, self.date_of_birth.day):
            employee_age += 1
        return employee_age

    def __str__(self) -> str:
        """Returns string of Employee object with details of name, date of birth, sex and age"""
        return f'{self.name}, {self.date_of_birth}, {self.sex}, {self.get_age()}'
