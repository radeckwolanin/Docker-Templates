from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hellow": "Digital World Again"}