from src.database.database_config import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, datetime
from sqlalchemy import DateTime, Date, Integer


class LeituraModel(Base):
    __tablename__ = "leitura"

    id: Mapped[str] = mapped_column(primary_key=True)

    data_anterior: Mapped[date] = mapped_column(Date, nullable=False)

    marcacao_anterior: Mapped[int] = mapped_column(Integer, nullable=False)

    data_atual: Mapped[date] = mapped_column(Date, nullable=False)

    marcacao_atual: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    # Relacionamento Fatura
    fatura: Mapped["FaturaModel"] = relationship(back_populates="leitura")  # type: ignore
    # ================
