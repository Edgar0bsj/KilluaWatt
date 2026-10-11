from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.module.item.item_controller import ItemController
from src.module.item.item_dto import ItemResponse, ItemRequest

router = APIRouter(prefix="/item", tags=["Item"])


def get_controller():
    return ItemController()


#
#
#
#
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(
    req: ItemRequest, controller: ItemController = Depends(get_controller)
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
async def update_item(
    id: str, req: ItemRequest, controller: ItemController = Depends(get_controller)
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
    nome: str | None = None, controller: ItemController = Depends(get_controller)
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
async def delete_item(id: str, controller: ItemController = Depends(get_controller)):
    try:
        res = controller.delete(id=id)

        if res:
            return

        return JSONResponse(status_code=401, content="Item não encontrado")

    except Exception:
        return JSONResponse(status_code=500, content="Error inesperado")
