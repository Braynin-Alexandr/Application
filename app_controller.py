from database import session, db_name, Base, engine
from models import Employee
import os
from itertools import chain
from utilts import employee_generator
from time import time
from datetime import datetime


class AppController:
    """Implement base commands of app"""
    @staticmethod
    def create_tables() -> None:
        """Creates employees table in the database"""
        if os.path.isfile(db_name):
            print(f'{db_name} already exists')
        else:
            Base.metadata.create_all(engine)
            print(f'{db_name} created')

    @staticmethod
    def add_employee(name: str, date_of_birth: str, sex: str) -> None:
        """Adds a new employee to the database"""
        try:
            new_employee = Employee(name=name, date_of_birth=date_of_birth, sex=sex)
            session.add(new_employee)
            session.commit()
            print(f'\"{name}\" added to {db_name}')

        except Exception as e:
            session.rollback()
            print(f'Error: {e}')
        finally:
            session.close()

    @staticmethod
    def add_employees() -> None:
        """Add a lot of employees to database"""
        employees = chain(
            employee_generator(999_900),
            employee_generator(100, start_letter='F', gender='Male')
        )
        try:
            employees = list(employees)
            batch_size = 10000
            for i in range(0, len(employees), batch_size):
                session.bulk_insert_mappings(Employee, employees[i:i+batch_size])
                session.commit()

        except Exception as e:
            session.rollback()
            print(f'Error: {e}')
        finally:
            session.close()

    @staticmethod
    def get_all_employees() -> None:
        """
        Displays all unique employees by name and date of birth from the database.
        Employees are sorted by name.
         """
        try:
            all_employees = (session.query(Employee).
                             group_by(Employee.name, Employee.date_of_birth).
                             order_by(Employee.name))

            if not all_employees.first():
                print("No employees found")
                return

            for employee in all_employees.yield_per(10000):
                print(employee)

        except Exception as e:
            session.rollback()
            print(f'Error: {e}')
        finally:
            session.close()

    @staticmethod
    def get_special_employees() -> None:
        """Returns all employees with male sex and last name starting with 'F'"""
        try:
            t1 = time()

            employees = session.query(Employee).filter(
                Employee.sex == 'Male',
                Employee.name.like('F%'))

            t2 = time()
            execution_time = t2 - t1

            if not employees.first():
                print("No employees found")
                return

            print(f'Execution time: {execution_time} seconds')

            with open('report.txt', mode='a+', encoding='utf-8') as f:
                f.write(f'{datetime.now()}, execution time: {execution_time} seconds\n')

        except Exception as e:
            session.rollback()
            print(f'Error: {e}')
        finally:
            session.close()
