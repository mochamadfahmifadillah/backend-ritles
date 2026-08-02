from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Assessment(Base):
    __tablename__ = "assessments"

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

    sleep_duration = Column(
        Float,
        nullable=False
    )

    study_duration = Column(
        Float,
        nullable=False
    )

    device_usage = Column(
        Float,
        nullable=False
    )

    task_load = Column(
        Float,
        nullable=False
    )

    risk_level = Column(
        String,
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="assessments"
    )