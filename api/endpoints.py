#from fastapi import APIRouter
#from fastapi import Depends
#from sqlalchemy.orm import Session
#from database import SessionLocal
#
#import models
#from models import ReviewsResponse
#from services.rutube import RutubeService
#
#router = APIRouter()
#
#
#@router.post("/sync/force/", response_model=ReviewsResponse)
#def get_reviews():
#    # Получаем ВСЕ видео (со всех страниц)
#    videos_data = RutubeService.get_all_channel_videos()  # ← Новый метод!
#
#    # Фильтруем отзывы
#    reviews = RutubeService.filter_reviews(videos_data)
#
#    return {
#        "reviews": reviews,
#        "total": len(reviews)
#    }
#
#@router.get("/reviews/", response_model=ReviewsResponse)
#def get_reviews(db: Session = Depends(SessionLocal)):
#    # Теперь берем данные из БД, а не из Rutube
#    reviews = db.query(models.VideoReview).all()
#
#    return {
#        "reviews": [{
#            "id": r.video_id,
#            "title": r.title,
#            "url": r.url,
#            "views": r.views,
#            "duration": r.duration
#        } for r in reviews],
#        "total": len(reviews)
#    }