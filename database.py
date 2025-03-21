from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_name = 'database.db'
engine = create_engine(f'sqlite:///{db_name}')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
