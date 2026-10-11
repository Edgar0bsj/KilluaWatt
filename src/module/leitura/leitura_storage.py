from datetime import date

from sqlalchemy import select

from src.database.database_config import create_database, SessionLocal
from src.module.leitura.leitura_model import LeituraModel


class LeituraStorage:
    def __init__(self):
        create_database()

    #
    #
    #
    #
    def create(
        self,
        id: str,
        data_anterior: date,
        marcacao_anterior: int,
        data_atual: date,
        marcacao_atual: int,
    ) -> "LeituraModel":

        with SessionLocal() as session:

            leitura = LeituraModel(
                id=id,
                data_anterior=data_anterior,
                marcacao_anterior=marcacao_anterior,
                data_atual=data_atual,
                marcacao_atual=marcacao_atual,
            )

            session.add(leitura)
            session.commit()

            session.refresh(leitura)

            return leitura

    #
    #
    #
    #
    def update(
        self,
        id: str,
        data_anterior: date,
        marcacao_anterior: int,
        data_atual: date,
        marcacao_atual: int,
    ) -> "LeituraModel":

        with SessionLocal() as session:

            leitura = session.get(LeituraModel, id)

            if not leitura:
                return None

            leitura.data_anterior = data_anterior
            leitura.marcacao_anterior = marcacao_anterior
            leitura.data_atual = data_atual
            leitura.marcacao_atual = marcacao_atual

            session.commit()
            session.refresh(leitura)

            return leitura

    #
    #
    #
    #
    def find_all(self) -> list["LeituraModel"]:
        with SessionLocal() as session:

            statement = select(LeituraModel)

            leituras = session.scalars(statement).all()

            return leituras

    #
    #
    #
    #
    def find_by_id(self, id: str) -> "LeituraModel":

        with SessionLocal() as session:
            return session.get(LeituraModel, id)

    #
    #
    #
    #
    def delete(self, id: str) -> bool:

        with SessionLocal() as session:

            entity = session.get(LeituraModel, id)

            if not entity:
                return False

            session.delete(entity)
            session.commit()

            return True

    #
    #
    #
    #
    def find_by_data_atual(self, data_atual: date) -> "LeituraModel":

        with SessionLocal() as session:
            statement = select(LeituraModel).where(
                LeituraModel.data_atual == data_atual
            )

            relogio = session.scalar(statement)

            return relogio
