from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    full_name = Column(
        String,
        nullable=False,
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
    )

    password = Column(
        String,
        nullable=False,
    )

    assessments = relationship(
        "Assessment",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    predictions = relationship(
        "Prediction",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    activity_notes = relationship(
        "ActivityNote",
        back_populates="user",
        cascade="all, delete-orphan",
    )