from sqlalchemy.orm import Session
from model.image import Image, ImageResponse, ImageLog
import datetime


def save(db: Session, image: Image, res: ImageResponse):
    image_log = ImageLog(
        image_path=image.path,
        success=res.success,
        message=res.message,
        class_=res.estimated_data.class_,
        confidence=res.estimated_data.confidence,
        request_timestamp=datetime.datetime.today(),
        response_timestamp=datetime.datetime.today(),
    )
    db.add(image_log)
    db.commit()
