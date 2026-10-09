from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(title="DAN API", description="Digital Awareness Network Backend")

# Configuração de CORS (Permitir frontend local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Para desenvolvimento local, depois deve ser restrito
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
