from pydantic import BaseModel, Field
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.dialects.mysql import DATETIME, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
import datetime
from typing import Optional

class Image(BaseModel):
    path: str

class EstimatedData(BaseModel):
    class_: Optional[int] = Field(alias="class", default=None)
    confidence: Optional[float] = None

class ImageResponse(BaseModel):
    success: bool
    message: str
    estimated_data: EstimatedData

Base = declarative_base()

class ImageLog(Base):
    __tablename__ = "ai_analysis_log"

    id:int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_path: str = Column(String(255))
    success: int = Column(Integer)
    message: str = Column(String(255))
    class_: int = Column("class", Integer)
    confidence: float = Column(DECIMAL)
    request_timestamp: datetime = Column(DATETIME)
    response_timestamp: datetime = Column(DATETIME)
    
    class Config:
        arbitrary_types_allowed = True