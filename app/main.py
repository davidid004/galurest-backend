from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user, reservation, invoice, category, dish
from app.routers import users


app = FastAPI(title="Galurest API")
app.include_router(users.router)


# Crear todas las tablas registradas en Base
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Galurest API funcionando"}