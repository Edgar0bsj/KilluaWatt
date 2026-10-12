from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.database.database_config import create_database, SessionLocal
from src.module.fatura.fatura_model import FaturaModel
from src.module.item.item_model import ItemModel


class FaturaStorage:
    def __init__(self):
        create_database()

    #
    #
    #
    #
    def create(
        self,
        id: str,
        nome: str,
        isPago: bool,
        relogio_id: str,
        leitura_id: str,
        itens: list[str],
    ) -> "FaturaModel":

        with SessionLocal() as session:

            itens_db = session.query(ItemModel).filter(ItemModel.id.in_(itens)).all()

            fatura = FaturaModel(
                id=id,
                nome=nome,
                isPago=isPago,
                relogio_id=relogio_id,
                leitura_id=leitura_id,
            )

            fatura.itens = itens_db

            session.add(fatura)
            session.commit()

            session.refresh(fatura)

            return fatura

    #
    #
    #
    #
    def update(
        self,
        id: str,
        nome: str,
        isPago: bool,
        relogio_id: str,
        leitura_id: str,
        itens: list[str],
    ) -> "FaturaModel":

        with SessionLocal() as session:

            fatura = session.get(FaturaModel, id)

            if not fatura:
                return None

            itens_db = session.query(ItemModel).filter(ItemModel.id.in_(itens)).all()

            fatura.nome = nome
            fatura.isPago = isPago
            fatura.relogio_id = relogio_id
            fatura.leitura_id = leitura_id

            fatura.itens = itens_db

            session.commit()
            session.refresh(fatura)

            return fatura

    #
    #
    #
    #
    def find_all(self) -> list["FaturaModel"]:
        with SessionLocal() as session:

            statement = (
                select(FaturaModel)
                .options(selectinload(FaturaModel.leitura))
                .options(selectinload(FaturaModel.relogio))
                .options(selectinload(FaturaModel.itens))
            )

            faturas = session.scalars(statement).all()

            return faturas

    #
    #
    #
    #
    def find_by_id(self, id: str) -> "FaturaModel":

        with SessionLocal() as session:
            return session.get(FaturaModel, id)

    #
    #
    #
    #
    def delete(self, id: str) -> bool:

        with SessionLocal() as session:

            entity = session.get(FaturaModel, id)

            if not entity:
                return False

            session.delete(entity)
            session.commit()

            return True

    #
    #
    #
    #
    def find_by_nome(self, nome: str) -> "FaturaModel":

        with SessionLocal() as session:
            statement = select(FaturaModel).where(FaturaModel.nome == nome)

            relogio = session.scalar(statement)

            return relogio
