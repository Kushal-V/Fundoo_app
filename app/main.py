from fastapi import FastAPI
from db.base import Base
from db.session import engine
from routes import user_route, note_route

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fundoo App Backend")

app.include_router(user_route.router)
app.include_router(note_route.router)
