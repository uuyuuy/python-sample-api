from fastapi import APIRouter, Depends
from model.image import Image
from service.image import search
from sqlalchemy.orm import Session
from repository.init import get_session

router = APIRouter()


@router.post("/")
def search_image_class(image: Image, db: Session = Depends(get_session)):
    res = search(db, image)
    return {"result": res.success}
