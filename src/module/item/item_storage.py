from sqlalchemy import select

from src.database.database_config import create_database, SessionLocal
from src.module.item.item_model import ItemModel


class ItemStorage:
    def __init__(self):
        create_database()

    #
    #
    #
    #
    def create(self, id: str, nome: str, valor: float) -> "ItemModel":

        with SessionLocal() as session:

            item = ItemModel(id=id, nome=nome, valor=valor)

            session.add(item)
            session.commit()

            session.refresh(item)

            return item

    #
    #
    #
    #
    def update(self, id: str, nome: str, valor: float) -> "ItemModel":

        with SessionLocal() as session:

            item = session.get(ItemModel, id)

            if not item:
                return None

            item.nome = nome
            item.valor = valor

            session.commit()
            session.refresh(item)

            return item

    #
    #
    #
    #
    def find_all(self) -> list["ItemModel"]:
        with SessionLocal() as session:

            statement = select(ItemModel)

            parans = session.scalars(statement).all()

            return parans

    #
    #
    #
    #
    def find_by_id(self, id: str) -> "ItemModel":

        with SessionLocal() as session:
            return session.get(ItemModel, id)

    #
    #
    #
    #
    def delete(self, id: str) -> bool:

        with SessionLocal() as session:

            entity = session.get(ItemModel, id)

            if not entity:
                return False

            session.delete(entity)
            session.commit()

            return True

    #
    #
    #
    #
    def find_by_nome(self, nome: str) -> "ItemModel":

        with SessionLocal() as session:
            statement = select(ItemModel).where(ItemModel.nome == nome)

            relogio = session.scalar(statement)

            return relogio
