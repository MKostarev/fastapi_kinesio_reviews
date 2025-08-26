from fastapi import FastAPI
from app.endpoints import reviews
from app.database import engine, Base

import logging
import sys

# Настраиваем логирование с правильной кодировкой
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        # Хендлер для консоли с UTF-8
        logging.StreamHandler(sys.stdout),
        # Хендлер для файла с UTF-8
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)


logger = logging.getLogger(__name__)


# СОЗДАЕМ ТАБЛИЦЫ В БД - ЭТО ДОЛЖНО БЫТЬ В САМОМ НАЧАЛЕ
Base.metadata.create_all(bind=engine)

# Создаем экземпляр приложения FastAPI
app = FastAPI(
    title="Rutube Microservice",
    description="Микросервис для сбора отзывов с Rutube",
    version="0.1.0"
)

# Подключаем роутеры
app.include_router(reviews.router)

# Самый простой эндпоинт для проверки, что всё работает
@app.get("/")
async def root():
    return {"message": "Rutube Microservice работает!!"}

# Эндпоинт для проверки здоровья сервиса (пригодится для мониторинга)
@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/test_branch")
async def health_check():
    return {"status": "OK"}



