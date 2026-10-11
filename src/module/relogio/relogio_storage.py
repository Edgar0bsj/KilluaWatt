from sqlalchemy import select

from src.database.database_config import create_database, SessionLocal
from src.module.relogio.relogio_dto import RelogioRequest
from src.module.relogio.relogio_model import RelogioModel


class RelogioStorage:
    def __init__(self):
        create_database()

    #
    #
    #
    #
    def create(self, id: str, nome: str, codigo: int) -> "RelogioModel":

        with SessionLocal() as session:

            relogio = RelogioModel(id=id, nome=nome, codigo=codigo)

            session.add(relogio)
            session.commit()

            session.refresh(relogio)

            return relogio

    #
    #
    #
    #
    def update(self, id: str, nome: str, codigo: int) -> "RelogioModel":

        with SessionLocal() as session:

            relogio = session.get(RelogioModel, id)

            if not relogio:
                return None

            relogio.nome = nome
            relogio.codigo = codigo

            session.commit()
            session.refresh(relogio)

            return relogio

    #
    #
    #
    #
    def find_all(self) -> list["RelogioModel"]:
        with SessionLocal() as session:

            statement = select(RelogioModel)

            parans = session.scalars(statement).all()

            return parans

    #
    #
    #
    #
    def find_by_id(self, id: str) -> "RelogioModel":

        with SessionLocal() as session:
            return session.get(RelogioModel, id)

    #
    #
    #
    #
    def delete(self, id: str) -> bool:

        with SessionLocal() as session:

            entity = session.get(RelogioModel, id)

            if not entity:
                return False

            session.delete(entity)
            session.commit()

            return True

    #
    #
    #
    #
    def find_by_cod(self, relogio_codigo: int) -> "RelogioModel":

        with SessionLocal() as session:
            statement = select(RelogioModel).where(
                RelogioModel.codigo == relogio_codigo
            )

            relogio = session.scalar(statement)

            return relogio
