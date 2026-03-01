from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base



engine = create_engine("sqlite:///./cards.db")

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(engine)