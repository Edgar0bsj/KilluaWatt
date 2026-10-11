from datetime import date

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.module.leitura.leitura_controller import LeituraController
from src.module.leitura.leitura_dto import LeituraRequest

router = APIRouter(prefix="/leitura", tags=["Leitura"])


def get_controller():
    return LeituraController()


#
#
#
#
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_leitura(
    req: LeituraRequest, controller: LeituraController = Depends(get_controller)
):
    try:
        res = controller.create(req)
        return res

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")


#
#
#
#
@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_leitura(
    id: str,
    req: LeituraRequest,
    controller: LeituraController = Depends(get_controller),
):
    try:
        res = controller.update(id=id, req=req)
        return res

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")


#
#
#
#
@router.get("/", status_code=status.HTTP_200_OK)
async def find_all_item(
    data_atual: date | None = None,
    controller: LeituraController = Depends(get_controller),
):
    try:
        res = controller.find_all(data_atual=data_atual)
        return res

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")


#
#
#
#
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id: str, controller: LeituraController = Depends(get_controller)):
    try:
        res = controller.delete(id=id)

        if res:
            return

        return JSONResponse(status_code=401, content="Leitura não encontrado")

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")
