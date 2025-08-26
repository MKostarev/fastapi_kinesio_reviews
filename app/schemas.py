from pydantic import BaseModel
from datetime import datetime
from typing import List


# Схема для ответа API
class VideoReviewResponse(BaseModel):
    id: int
    source_id: str
    source: str
    title: str
    url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Для совместимости с ORM


class ReviewsResponse(BaseModel):
    reviews: List[VideoReviewResponse]
    total: int


class TaskStartedResponse(BaseModel):
    message: str
    task: str