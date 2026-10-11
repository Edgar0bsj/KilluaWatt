from src.module.item.item_service import ItemService
from src.module.item.item_model import ItemModel
from src.module.item.item_dto import ItemRequest, ItemResponse


class ItemController:
    def __init__(self):
        self.service = ItemService()

    #
    #
    #
    #
    def create(self, req: ItemRequest) -> ItemModel:
        return self.service.create_item(nome=req.nome, valor=req.valor)

    #
    #
    #
    #
    def update(self, id: str, req: ItemRequest) -> ItemModel:
        return self.service.update_item(id=id, nome=req.nome, valor=req.valor)

    #
    #
    #
    #
    def find_all(self, nome: str | None = None) -> list[ItemModel]:
        if nome:
            return self.service.find_all_item(nome)

        return self.service.find_all_item()

    #
    #
    #
    #
    def delete(self, id: str) -> bool:
        return self.service.delete_item(id)
