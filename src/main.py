from fastapi import FastAPI
from src.router.relogio_router import router as relogio_router
from src.router.item_route import router as item_router

app = FastAPI()

app.include_router(relogio_router)
app.include_router(item_router)
