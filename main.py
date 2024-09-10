from fastapi import FastAPI
from api import image

app = FastAPI()
app.include_router(image.router)
