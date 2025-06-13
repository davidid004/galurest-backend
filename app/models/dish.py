from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.db.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    dish_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(7, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id", ondelete="SET NULL"), nullable=True)
