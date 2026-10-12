from src.module.fatura.fatura_service import FaturaService
from src.module.fatura.fatura_model import FaturaModel
from src.module.fatura.fatura_dto import FaturaRequest


class FaturaController:
    def __init__(self):
        self.service = FaturaService()

    #
    #
    #
    #
    def create(self, req: FaturaRequest) -> FaturaModel:
        return self.service.create_fatura(
            nome=req.nome,
            isPago=req.isPago,
            relogio_id=req.relogio_id,
            leitura_id=req.leitura_id,
            itens=req.itens,
        )

    #
    #
    #
    #
    def update(self, id: str, req: FaturaRequest) -> FaturaModel:
        return self.service.update_item(
            id=id,
            nome=req.nome,
            isPago=req.isPago,
            relogio_id=req.relogio_id,
            leitura_id=req.leitura_id,
            itens=req.itens,
        )

    #
    #
    #
    #
    def find_all(self, nome: str | None = None) -> list[FaturaModel]:
        if nome:
            return self.service.find_all_item(nome)

        return self.service.find_all_item()

    #
    #
    #
    #
    def delete(self, id: str) -> bool:
        return self.service.delete_item(id)
