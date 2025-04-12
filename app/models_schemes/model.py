from app.dev.database import Base
from sqlalchemy import Column, INTEGER, String


class Memos(Base):
    __tablename__ = "memos"

    id = Column(INTEGER, primary_key=True, index=True)
