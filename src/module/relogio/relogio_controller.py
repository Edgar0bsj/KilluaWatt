from src.module.relogio.relogio_service import RelogioService
from src.module.relogio.relogio_dto import RelogioRequest


class RelogioController:

    def __init__(self):
        self.service = RelogioService()

    #
    #
    #
    #
    def create_relogio(self, req: RelogioRequest):
        res = self.service.create_relogio(nome=req.nome, codigo=req.codigo)

        return res

    #
    #
    #
    #
    def find_all(self, codigo: int | None = None):
        if codigo:
            return self.service.find_by_codigo(codigo)

        return self.service.find_all()

    #
    #
    #
    #
    def update_relogio(self, id: str, req: RelogioRequest):
        self.service.update_relogio(id=id, nome=req.nome, codigo=req.codigo)

    #
    #
    #
    #
    def delete_relogio(self, id: str):
        return self.service.delete(id)
