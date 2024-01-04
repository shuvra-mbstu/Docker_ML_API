from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "success": True,
        "message": "pong!"
        }