from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from assistant_core.brain import get_response

app = FastAPI()

# ADD THIS CORS PART
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.get("/assistant")
def assistant(query: str = "hello"):
    reply = get_response(query)
    return {"response": reply}
