from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Nama" : "Alessandro JH",
        "NIM" : "18222025",
        "Bisnis" : "ToFood",
        "Recipe" : "Soto Barbeque",
        "Recipe Screening": "Passed",
        "Recipe Recomendation": "Add more spicess"
            }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}