from fastapi import FastAPI
from routes import user_route
from db.base import Base
from db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fundoo App Backend")

app.include_router(user_route.router)
