from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URl = "sqlite:///./testmemo.db"

engine = create_engine(DATABASE_URl, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to get the database session:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
