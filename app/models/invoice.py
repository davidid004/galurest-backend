from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey
from app.db.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey("reservations.reservation_id", ondelete="CASCADE"), nullable=False, unique=True)
    total = Column(Numeric(10, 2), nullable=False)
    issued_date = Column(Date, nullable=False)
