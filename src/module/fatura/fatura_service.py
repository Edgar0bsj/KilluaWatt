from src.module.fatura.fatura_storage import FaturaStorage
from src.module.fatura.fatura_model import FaturaModel
from uuid import uuid4, UUID


class FaturaService:
    def __init__(self):
        self.repo = FaturaStorage()

    #
    #
    #
    #
    def create_fatura(
        self,
        nome: str,
        isPago: bool,
        relogio_id: str | UUID,
        leitura_id: str | UUID,
        itens: list[str] | list[UUID],
    ) -> FaturaModel:

        return self.repo.create(
            id=str(uuid4()),
            nome=nome,
            isPago=isPago,
            relogio_id=relogio_id,
            leitura_id=leitura_id,
            itens=itens,
        )

    #
    #
    #
    #
    def update_item(
        self,
        id: str,
        nome: str,
        isPago: bool,
        relogio_id: str,
        leitura_id: str,
        itens: list[str],
    ) -> FaturaModel:

        return self.repo.update(
            id=id,
            nome=nome,
            isPago=isPago,
            relogio_id=relogio_id,
            leitura_id=leitura_id,
            itens=itens,
        )

    #
    #
    #
    #
    def find_all_item(self, nome: str | None = None) -> list[FaturaModel]:
        if nome:
            return self.repo.find_by_nome(nome)

        return self.repo.find_all()

    #
    #
    #
    #
    def delete_item(self, id: str) -> bool:
        return self.repo.delete(id)
