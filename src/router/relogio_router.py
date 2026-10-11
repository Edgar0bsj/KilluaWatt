from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.module.relogio.relogio_controller import RelogioController
from src.module.relogio.relogio_dto import RelogioRequest

router = APIRouter(prefix="/relogio", tags=["Relogio"])


def get_controller():
    return RelogioController()


#
#
#
#
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_relogio(
    req: RelogioRequest, controller: RelogioController = Depends(get_controller)
):
    try:
        controller.create_relogio(req)
        return {"msg": "Relogio criado com sucesso!"}

    except IntegrityError as err:
        return JSONResponse(
            status_code=400,
            content={"message": "Codigo do relogio já existe no banco de dados"},
        )

    except Exception as err:

        return JSONResponse(
            status_code=500,
            content={"message": "Error inesperado"},
        )


#
#
#
#
@router.get("/", status_code=status.HTTP_200_OK)
async def find_all_relogio(
    codigo: int | None = None, controller: RelogioController = Depends(get_controller)
):
    try:
        if codigo:
            res = controller.find_all(codigo)

        else:
            res = controller.find_all()

        return res

    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"message": "Error inesperado"},
        )


#
#
#
#
@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_relogio(
    id: str,
    req: RelogioRequest,
    controller: RelogioController = Depends(get_controller),
):
    try:
        controller.update_relogio(id=id, req=req)

        return JSONResponse(
            status_code=200,
            content={"message": "Relogio atualizado com sucesso!"},
        )

    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"message": "Error inesperado"},
        )


#
#
#
#
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_relogio(
    id: str,
    controller: RelogioController = Depends(get_controller),
):
    try:
        result = controller.delete_relogio(id=id)

        if not result:
            return JSONResponse(
                status_code=401,
                content="Relogio não encontrado",
            )

        return JSONResponse(
            status_code=204,
            content="",
        )

    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"message": "Error inesperado"},
        )
