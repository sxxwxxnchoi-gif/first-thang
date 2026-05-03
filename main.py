from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "May 3th not happy"}
