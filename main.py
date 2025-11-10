from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{ "message": "Study read is working!"}

@app.get("/healthz")
def healthz():
    return{ "status": "ok"}