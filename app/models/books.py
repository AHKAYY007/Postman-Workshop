from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author = Column(String, index=True)
    published = Column(Boolean)