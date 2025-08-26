#import requests
#from core.config import CHANNEL_ID
#
#
#class RutubeService:
#    @staticmethod
#    def get_all_channel_videos():
#        all_videos = []
#        page = 1
#
#        while True:
#            url = f"https://rutube.ru/api/channel/{CHANNEL_ID}/?page={page}"
#            response = requests.get(url)
#            data = response.json()
#
#            if not data.get("results"):
#                break
#            all_videos.extend(data["results"])
#
#            # Проверяем есть ли следующая страница
#            if not data.get("next"):
#                break
#            page += 1
#        return {"results": all_videos}
#
#    @staticmethod
#    def filter_reviews(videos_data: dict):
#        reviews = []
#        # Все формы слова "отзыв" для поиска
#        review_keywords = [
#            'отзыв', 'отзыва', 'отзыве', 'отзыву', 'отзывом',  # падежи
#            'отзывы', 'отзывов', 'отзывам', 'отзывами', 'отзывах',  # множественное число
#            'отз', 'отзив', 'отзивы'  # возможные опечатки
#        ]
#
#        for video in videos_data.get("results", []):
#            title = video.get("title", "").lower()
#            description = video.get("description", "").lower()
#
#            # Проверяем все формы слова
#            if any(keyword in title or keyword in description
#                   for keyword in review_keywords):
#                reviews.append({
#                    "id": video["id"],
#                    "title": video["title"],
#                    "url": f"https://rutube.ru/video/{video['id']}/",
#                    "views": video.get("hits", 0),
#                    "duration": video.get("duration", 0)
#                })
#        return reviews