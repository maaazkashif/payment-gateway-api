from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
from app.schemas import Role

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)   # 👈 Add this line
    role = Column(Enum(Role), nullable=False)

