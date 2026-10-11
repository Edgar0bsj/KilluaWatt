from datetime import date

from src.module.leitura.leitura_storage import LeituraStorage
from src.module.leitura.leitura_model import LeituraModel
from uuid import uuid4


class LeituraService:
    def __init__(self):
        self.repo = LeituraStorage()

    #
    #
    #
    #
    def create_leitura(
        self,
        data_anterior: date,
        marcacao_anterior: int,
        data_atual: date,
        marcacao_atual: int,
    ) -> LeituraModel:
        return self.repo.create(
            id=str(uuid4()),
            data_anterior=data_anterior,
            marcacao_anterior=marcacao_anterior,
            data_atual=data_atual,
            marcacao_atual=marcacao_atual,
        )

    #
    #
    #
    #
    def update_leitura(
        self,
        id: str,
        data_anterior: date,
        marcacao_anterior: int,
        data_atual: date,
        marcacao_atual: int,
    ) -> LeituraModel:
        return self.repo.update(
            id=id,
            data_anterior=data_anterior,
            marcacao_anterior=marcacao_anterior,
            data_atual=data_atual,
            marcacao_atual=marcacao_atual,
        )

    #
    #
    #
    #
    def find_all_leitura(self, data_atual: date | None = None) -> list[LeituraModel]:
        if data_atual:
            return self.repo.find_by_data_atual(data_atual)

        return self.repo.find_all()

    #
    #
    #
    #
    def delete_leitura(self, id: str) -> bool:
        return self.repo.delete(id)
