from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from ..database import Base


class Bookmark(Base):
    __tablename__ = "bookmark"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    url = Column(String, unique=True, index=True)
    date_created = Column(DateTime, default=datetime.now())
