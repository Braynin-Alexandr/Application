import random
from faker import Faker

fake = Faker()


def generate_last_name(start_letter: str, sex: str) -> str:
    """Returns last name that starts with a specific letter"""

    for _ in range(1000):
        last_name = fake.last_name_male() if sex == "Male" else fake.last_name_female()
        if last_name.startswith(start_letter.upper()):
            return last_name
    raise ValueError(f'No last name found starting with "{start_letter}"')


def employee_generator(count: int, start_letter: str = None, gender: str = None):
    """Generates fake employees"""
    for _ in range(count):
        sex = gender if gender else random.choice(["Male", "Female"])

        if start_letter:
            last_name = generate_last_name(start_letter, sex)
        else:
            last_name = fake.last_name_male() if sex == "Male" else fake.last_name_female()

        first_name = fake.first_name_male() if sex == "Male" else fake.first_name_female()
        full_name = f'{last_name} {first_name}'

        yield {'name': full_name,
               'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=65),
               'sex': sex}
