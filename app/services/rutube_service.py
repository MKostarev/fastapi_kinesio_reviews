from sqlalchemy.orm import Session
from app import models
from app.services.notification_service import NotificationService

# Моковые данные - имитация ответа от Rutube API
MOCK_VIDEOS_DATA = [
    {
        "video_id": "12345",
        "title": "Отзыв о продукте - это просто великолепно!",
        "url": "https://rutube.ru/video/12345/",
        "views": 1000
    },
    {
        "video_id": "67890",
        "title": "Обзор нового фитнес-тренажера",
        "url": "https://rutube.ru/video/67890/",
        "views": 500
    },
    {
        "video_id": "11111",
        "title": "Мой честный отзыв после месяца использования",
        "url": "https://rutube.ru/video/11111/",
        "views": 1500
    },
    {
        "video_id": "99999",
        "title": "Просто развлекательное видео",
        "url": "https://rutube.ru/video/99999/",
        "views": 2000
    }
]


def get_all_channel_videos():
    """Заглушка: возвращает моковые данные вместо реального API Rutube"""
    print("🔧 Используются моковые данные Rutube")
    return MOCK_VIDEOS_DATA


def filter_reviews(videos_data):
    """Фильтрует видео, оставляя только отзывы (по ключевым словам в title)"""
    keywords = ["отзыв", "отзывы", "отзыву"]
    reviews = []

    for video in videos_data:
        title_lower = video["title"].lower()
        if any(keyword in title_lower for keyword in keywords):
            reviews.append(video)

    print(f"🎯 Найдено {len(reviews)} отзывов из {len(videos_data)} видео")
    return reviews


def update_db_with_reviews(db: Session, reviews_data):
    """Обновляет базу данных с найденными отзывами"""
    new_count = 0
    updated_count = 0
    new_ids = []

    for review in reviews_data:
        # Проверяем, существует ли уже такое видео в БД
        db_review = db.query(models.VideoReview).filter(
            models.VideoReview.source_id == review["video_id"]
        ).first()

        if db_review:
            # Обновляем существующую запись
            if db_review.title != review["title"] or db_review.url != review["url"]:
                db_review.title = review["title"]
                db_review.url = review["url"]
                updated_count += 1
        else:
            # Создаем новую запись
            new_review = models.VideoReview(
                source_id=review["video_id"],
                title=review["title"],
                url=review["url"]
            )
            db.add(new_review)
            new_count += 1
            new_ids.append(review["video_id"])

    db.commit()

    results = {
        "new": new_count,
        "updated": updated_count,
        "total": new_count + updated_count,
        "new_ids": new_ids
    }

    print(f"💾 База обновлена: {new_count} новых, {updated_count} обновленных записей")
    return results