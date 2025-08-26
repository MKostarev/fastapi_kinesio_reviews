from datetime import datetime
#from sqlalchemy.orm import Session
#from . import models


#def get_review_by_video_id(db: Session, video_id: str):
#    return db.query(models.VideoReview).filter(models.VideoReview.video_id == video_id).first()


#def create_or_update_review(db: Session, review_data: dict):
#    # Проверяем есть ли уже видео
#    existing = get_review_by_video_id(db, review_data["id"])
#
#    if existing:
#        # Обновляем просмотры
#        existing.views = review_data["views"]
#        existing.updated_at = datetime.utcnow()
#    else:
#        # Создаем новую запись
#        db_review = models.VideoReview(
#            video_id=review_data["id"],
#            title=review_data["title"],
#            url=review_data["url"],
#            views=review_data["views"],
#            duration=review_data["duration"]
#        )
#        db.add(db_review)
#
#    db.commit()