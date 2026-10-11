from src.database.database_config import Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, String, Float


class ItemModel(Base):
    __tablename__ = "item"

    id: Mapped[str] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False)

    valor: Mapped[float] = mapped_column(Float, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
