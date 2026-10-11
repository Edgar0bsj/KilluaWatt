from datetime import date

from pydantic import BaseModel


class LeituraRequest(BaseModel):
    data_anterior: date
    marcacao_anterior: int
    data_atual: date
    marcacao_atual: int
