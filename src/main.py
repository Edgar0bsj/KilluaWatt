from fastapi import FastAPI
from src.router.relogio_router import router as relogio_router
from src.router.item_route import router as item_router
from src.router.leitura_route import router as leitura_router
from src.router.fatura_route import router as fatura_router

app = FastAPI()

app.include_router(relogio_router)
app.include_router(item_router)
app.include_router(leitura_router)
app.include_router(fatura_router)
