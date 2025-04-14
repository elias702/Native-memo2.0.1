from .database import Base
from sqlalchemy import Column, INTEGER, String, DateTime, func


class Memos(Base):
    __tablename__ = "memos"

    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published_at = Column(DateTime, server_default=func.now())
