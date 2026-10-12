from src.database.database_config import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, String, Boolean

from src.module.item.item_model import item_fatura


class FaturaModel(Base):
    __tablename__ = "fatura"

    id: Mapped[str] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False)

    isPago: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Relacionamento Relogio
    relogio_id: Mapped[str] = mapped_column(ForeignKey("relogio.id"))
    relogio: Mapped["RelogioModel"] = relationship(back_populates="fatura")  # type: ignore
    # ================
    #
    #
    #
    # Relacionamento Leitura
    leitura_id: Mapped[str] = mapped_column(ForeignKey("leitura.id"))
    leitura: Mapped["LeituraModel"] = relationship(back_populates="fatura", cascade="all")  # type: ignore
    # ================
    #
    #
    #
    # Relacionamento Item
    # tabela associativa
    itens: Mapped[list["ItemModel"]] = relationship(  # type: ignore
        "ItemModel", secondary=item_fatura, back_populates="faturas"
    )
    # ================

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
