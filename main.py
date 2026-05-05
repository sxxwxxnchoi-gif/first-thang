from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "May 3th not happy"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"id": item_id, "message": "coding in Gangnam"}