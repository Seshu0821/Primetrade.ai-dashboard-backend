from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.profile import router as profile_router
from app.routes.tasks import router as tasks_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scalable FastAPI App")

# CORS FIX — MUST BE BEFORE INCLUDE_ROUTER
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can set your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],   # This is important for OPTIONS
    allow_headers=["*"],  
)

# Include Routers
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(tasks_router)
