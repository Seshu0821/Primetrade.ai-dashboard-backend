from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.profile import router as profile_router
from app.routes.tasks import router as tasks_router
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scalable FastAPI App")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(tasks_router)
