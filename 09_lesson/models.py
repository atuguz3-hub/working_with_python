from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Subject(Base):
    __tablename__ = "subject"

    subject_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    subject_title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
