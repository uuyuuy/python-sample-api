from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def get_image_path():
    return ""