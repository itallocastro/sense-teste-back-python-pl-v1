from fastapi import FastAPI
from .cep.router import router
app = FastAPI()

app.include_router(router)