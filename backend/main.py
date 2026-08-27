from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from routes import application, auth, grievance, health
except ModuleNotFoundError:
    from backend.routes import application, auth, grievance, health

app = FastAPI(
    title="PFGuide API",
    description="Synthetic PF claim guidance prototype. No live EPFO data is accessed.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://pf-guide-43dtgn8qw.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(application.router)
app.include_router(grievance.router)