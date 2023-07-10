from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
PG_USER = os.environ.get('PG_USER')
PG_PASSWORD = os.environ.get('PG_PASSWORD')
PG_DB = os.environ.get('PG_DB')

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASSWORD}@127.0.0.1:5431/{PG_DB}")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class Advert(Base):

    __tablename__ = 'advertisements'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    creation_date = Column(DateTime, server_default=func.now())

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)