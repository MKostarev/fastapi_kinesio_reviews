from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.services import rutube_service
from app.services.notification_service import NotificationService

# Убедись, что router создается здесь!
router = APIRouter(prefix="/api/v1", tags=["reviews"])


@router.get("/reviews/", response_model=schemas.ReviewsResponse)
def get_reviews(db: Session = Depends(get_db)):
    """Получить все отзывы из базы данных"""
    reviews = db.query(models.VideoReview).all()
    return {"reviews": reviews, "total": len(reviews)}


@router.post("/sync/force/", response_model=schemas.TaskStartedResponse)
def force_sync(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """Запустить принудительную синхронизацию (с моковыми данными)"""
    background_tasks.add_task(perform_sync, db, "manual")
    return {"message": "Фоновая задача синхронизации запущена", "task": "full_sync"}


def perform_sync(db: Session):
    """Фоновая задача для синхронизации"""
    print("🔄 Запуск синхронизации...")

    # 1. Получаем данные (пока моковые)
    videos_data = rutube_service.get_all_channel_videos()

    # 2. Фильтруем отзывы
    reviews = rutube_service.filter_reviews(videos_data)

    # 3. Сохраняем в БД
    rutube_service.update_db_with_reviews(db, reviews)

    print("✅ Синхронизация завершена")


def perform_sync(db: Session, source: str = "manual"):
    """Фоновая задача для синхронизации"""
    print("🔄 Запуск синхронизации...")

    try:
        # 1. Получаем данные (пока моковые)
        videos_data = rutube_service.get_all_channel_videos()

        # 2. Фильтруем отзывы
        reviews = rutube_service.filter_reviews(videos_data)

        if not reviews:
            print("ℹ️ Новых отзывов не найдено")
            NotificationService.no_new_data_notification(source)
            return

        # 3. Сохраняем в БД
        results = rutube_service.update_db_with_reviews(db, reviews)

        # 4. Отправляем уведомление о успешной синхронизации
        NotificationService.sync_completed_notification(results, source)

        print("✅ Синхронизация завершена успешно")

    except Exception as e:
        error_msg = f"Ошибка синхронизации: {str(e)}"
        print(f"❌ {error_msg}")
        NotificationService.sync_failed_notification(error_msg, source)
        raise e