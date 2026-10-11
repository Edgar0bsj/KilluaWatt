from src.module.relogio.relogio_storage import RelogioStorage
from src.module.relogio.relogio_dto import RelogioRequest, RelogioResponse
from uuid import uuid4


class RelogioService:
    def __init__(self):
        self.repo = RelogioStorage()

    #
    #
    #
    #
    def create_relogio(self, nome: str, codigo: int) -> None:

        self.repo.create(id=str(uuid4()), nome=nome, codigo=codigo)

        return

    #
    #
    #
    #
    def update_relogio(self, id: str, nome: str, codigo: int) -> None:

        self.repo.update(id=id, nome=nome, codigo=codigo)
        return

    #
    #
    #
    #
    def find_all(self) -> list[RelogioResponse]:
        relogios = self.repo.find_all()

        _buffer = []
        for elem in relogios:
            _temp = RelogioResponse(id=elem.id, nome=elem.nome, codigo=elem.codigo)
            _buffer.append(_temp)

        return _buffer

    #
    #
    #
    #
    def find_id(self, id: str) -> RelogioResponse:
        result = self.repo.find_by_id(id)

        if not result:
            return None

        return result

    #
    #
    #
    #
    def find_by_codigo(self, codigo: int):
        result = self.repo.find_by_cod(codigo)

        if not result:
            return []

        return result

    #
    #
    #
    #
    def delete(self, codigo: int) -> bool:
        return self.repo.delete(codigo)
