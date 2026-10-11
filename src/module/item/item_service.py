from src.module.item.item_storage import ItemStorage
from src.module.item.item_model import ItemModel
from uuid import uuid4


class ItemService:
    def __init__(self):
        self.repo = ItemStorage()

    #
    #
    #
    #
    def create_item(self, nome: str, valor: float) -> ItemModel:
        return self.repo.create(id=str(uuid4()), nome=nome, valor=valor)

    #
    #
    #
    #
    def update_item(self, id: str, nome: str, valor: float) -> ItemModel:
        return self.repo.update(id=id, nome=nome, valor=valor)

    #
    #
    #
    #
    def find_all_item(self, nome: str | None = None) -> list[ItemModel]:
        if nome:
            return self.repo.find_by_nome(nome)

        return self.repo.find_all()

    #
    #
    #
    #
    def delete_item(self, id: str) -> bool:
        return self.repo.delete(id)
