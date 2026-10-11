from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class ItemRequest(BaseModel):
    nome: Annotated[str, Field(min_length=3, max_length=50)]
    valor: float


class ItemResponse(BaseModel):
    id: UUID
    nome: Annotated[str, Field(min_length=3, max_length=50)]
    valor: float
