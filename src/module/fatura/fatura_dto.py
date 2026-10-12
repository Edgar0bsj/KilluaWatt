from typing import Annotated

from pydantic import BaseModel, Field


class FaturaRequest(BaseModel):
    nome: Annotated[str, Field(min_length=3, max_length=50)]
    isPago: bool = False
    relogio_id: str
    leitura_id: str
    itens: list[str]
