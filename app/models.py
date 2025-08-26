from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql import func
from app.database import Base

class VideoReview(Base):
    __tablename__ = "video_reviews"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String, unique=True, index=True)  # ID из Rutube
    source = Column(String, default="rutube")  # Источник данных
    title = Column(String)  # Название видео
    url = Column(String)  # Ссылка на видео
    created_at = Column(DateTime, default=func.now())  # Дата создания
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Дата обновления

    def __repr__(self):
        return f"<VideoReview {self.title}>"