from datetime import date

from src.module.leitura.leitura_service import LeituraService
from src.module.leitura.leitura_model import LeituraModel
from src.module.leitura.leitura_dto import LeituraRequest


class LeituraController:
    def __init__(self):
        self.service = LeituraService()

    #
    #
    #
    #
    def create(self, req: LeituraRequest) -> LeituraModel:
        return self.service.create_leitura(
            data_anterior=req.data_anterior,
            marcacao_anterior=req.marcacao_anterior,
            data_atual=req.data_atual,
            marcacao_atual=req.marcacao_atual,
        )

    #
    #
    #
    #
    def update(self, id: str, req: LeituraRequest) -> LeituraModel:
        return self.service.update_leitura(
            id=id,
            data_anterior=req.data_anterior,
            marcacao_anterior=req.marcacao_anterior,
            data_atual=req.data_atual,
            marcacao_atual=req.marcacao_atual,
        )

    #
    #
    #
    #
    def find_all(self, data_atual: date | None = None) -> list[LeituraModel]:
        if data_atual:
            return self.service.find_all_leitura(data_atual)

        return self.service.find_all_leitura()

    #
    #
    #
    #
    def delete(self, id: str) -> bool:
        return self.service.delete_leitura(id)
