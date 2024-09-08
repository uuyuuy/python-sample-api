from fastapi import FastAPI
from api import image

app = FastAPI()

def main():
    app = FastAPI()
    app.include_router(image.router)

if __name__ == "__main__":
    main()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}