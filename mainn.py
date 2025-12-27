from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="Elite Backend API",
    version="1.0.0",
    description="Clean, fast, production-ready backend"
)

# CORS (frontend friendly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# MODELS
# -------------------------
class HealthResponse(BaseModel):
    status: str
    time: str

class Message(BaseModel):
    message: str

# -------------------------
# ROUTES
# -------------------------
@app.get("/", response_model=HealthResponse)
def root():
    return {
        "status": "Backend is running 🚀",
        "time": datetime.now().isoformat()
    }

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.post("/echo")
def echo(data: Message):
    return {
        "received": data.message,
        "length": len(data.message)
    }

# -------------------------
# ENTRY CHECK
# -------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
