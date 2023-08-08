from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello You": "Digital World Again and again"}