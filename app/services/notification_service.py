import logging
from datetime import datetime
from typing import Dict, Any

# Настраиваем логирование
logger = logging.getLogger(__name__)


class NotificationService:
    @staticmethod
    def send_email_notification(subject: str, message: str):
        """
        Заглушка для отправки email-уведомлений.
        Пока просто логирует сообщение в консоль.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Форматированное сообщение для консоли (с emoji)
        console_message = f"\n📧 EMAIL NOTIFICATION [{timestamp}]\n"
        console_message += f"📭 Тема: {subject}\n"
        console_message += f"📄 Сообщение: {message}\n"
        console_message += "─" * 50

        # Простое сообщение для логгера (без emoji)
        log_message = f"\nEMAIL NOTIFICATION [{timestamp}]\n"
        log_message += f"Тема: {subject}\n"
        log_message += f"Сообщение: {message}\n"
        log_message += "-" * 50

        # Логируем без emoji
        logger.info(log_message)
        # Выводим в консоль с emoji
        print(console_message)

    @staticmethod
    def sync_completed_notification(results: Dict[str, Any], source: str = "manual"):
        """
        Специализированное уведомление о завершении синхронизации
        """
        subject = f"Синхронизация завершена ({source})"

        message = f"Результаты синхронизации:\n"
        message += f"• Новых записей: {results.get('new', 0)}\n"
        message += f"• Обновленных записей: {results.get('updated', 0)}\n"
        message += f"• Всего обработано: {results.get('total', 0)}\n"

        if results.get('new', 0) > 0 and results.get('new_ids'):
            message += f"• Добавлены записи: {results.get('new_ids', [])}\n"

        message += f"\nИсточник: {source}"

        NotificationService.send_email_notification(subject, message)

    @staticmethod
    def sync_failed_notification(error: str, source: str = "manual"):
        """
        Уведомление об ошибке синхронизации
        """
        subject = f"Ошибка синхронизации ({source})"
        message = f"Произошла ошибка во время синхронизации:\n{error}"

        NotificationService.send_email_notification(subject, message)

    @staticmethod
    def no_new_data_notification(source: str = "manual"):
        """
        Уведомление о том, что новых данных не найдено
        """
        subject = f"Новых данных не найдено ({source})"
        message = "В процессе синхронизации новых отзывов не обнаружено."

        NotificationService.send_email_notification(subject, message)