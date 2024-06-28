from fastapi import FastAPI
from routers.routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:5173",  # Zaktualizuj ten adres URL zgodnie z adresem Twojej aplikacji Vue
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Pozwól na wszystkie metody
    allow_headers=["*"],  # Pozwól na wszystkie nagłówki
)
app.include_router(router)