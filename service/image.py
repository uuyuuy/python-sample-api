from model.image import Image, ImageResponse
import requests
import config
from repository.image import save
from sqlalchemy.orm import Session

def search(db: Session, image: Image):
    try:
        response = requests.post("{url}".format(url=config.MOCK_API_URL))
    except requests.exceptions.RequestException as err:
        print(err)
        return

    res = ImageResponse(**response.json())
    save(db, image, res)

    return res