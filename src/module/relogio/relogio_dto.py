from dataclasses import dataclass
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class RelogioRequest(BaseModel):
    nome: Annotated[str, Field(min_length=3, max_length=50)]
    codigo: int


class RelogioResponse(BaseModel):
    id: UUID
    nome: Annotated[str, Field(min_length=3, max_length=50)]
    codigo: int
