from sqlalchemy import CheckConstraint, Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'staff')", name="check_user_role"),
    )