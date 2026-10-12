from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.module.fatura.fatura_controller import FaturaController
from src.module.fatura.fatura_dto import FaturaRequest

router = APIRouter(prefix="/fatura", tags=["Fatura"])


def get_controller():
    return FaturaController()


#
#
#
#
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_fatura(
    req: FaturaRequest, controller: FaturaController = Depends(get_controller)
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
async def update_fatura(
    id: str, req: FaturaRequest, controller: FaturaController = Depends(get_controller)
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
async def find_all_fatura(
    nome: str | None = None, controller: FaturaController = Depends(get_controller)
):
    try:
        res = controller.find_all(nome=nome)
        return res

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")


#
#
#
#
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fatura(
    id: str, controller: FaturaController = Depends(get_controller)
):
    try:
        res = controller.delete(id=id)

        if res:
            return

        return JSONResponse(status_code=401, content="Item não encontrado")

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")
