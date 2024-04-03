from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func


class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(String, default=func.now())
    details = Column(String)
    attendeeId = Column(String, ForeignKey("attendees.id"))

    def __repr__(self):
        return f"CheckIns [attendeeId={self.attendeeId}]"