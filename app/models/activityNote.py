from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ActivityNote(Base):

    __tablename__ = "activity_notes"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    title = Column(
        String,
        nullable=False
    )


    note = Column(
        Text,
        nullable=True
    )


    user = relationship(
        "User",
        back_populates="activity_notes"
    )