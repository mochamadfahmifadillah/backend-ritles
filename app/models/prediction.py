from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

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

    fatigue_score = Column(
        Float,
        nullable=True
    )

    risk_level = Column(
        String,
        nullable=True
    )

    model_version = Column(
        String,
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="predictions"
    )