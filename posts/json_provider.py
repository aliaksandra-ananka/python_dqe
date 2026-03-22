import os
import json
from .news import News
from .private_ad import PrivateAd
from .weather import WeatherUpdate
from .base import Post
from utils.text_utils import normalize_text, fix_iz_mistakes

class JSONProcessingError(Exception):
    """Custom exception for JSON processing errors"""
    pass

class JSONPostProvider:
    """Read posts from JSON file, normalize text, publish, then delete file"""

    def __init__(self, file_path=None):
        self.file_path = file_path or os.path.join("input", "posts.json")

    def process_file(self):
        if not os.path.exists(self.file_path):
            raise JSONProcessingError(f"File not found: {self.file_path}")

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                records = json.load(f)
        except Exception as e:
            raise JSONProcessingError(f"Error reading JSON file: {e}")

        for record in records:
            self._publish_from_dict(record)

        # удаляем файл после успешной обработки
        os.remove(self.file_path)
        print(f"File {self.file_path} processed and deleted.")

    def _publish_from_dict(self, record):
        post_type = record.get("type", "").lower()
        text = record.get("text", "")
        text = fix_iz_mistakes(normalize_text(text))

        if post_type == "news":
            city = record.get("city", "Unknown")
            post = News(text, city)
        elif post_type == "privatead":
            exp_date = record.get("expiration", "")
            post = PrivateAd(text, exp_date)
        elif post_type == "weather":
            temp = int(record.get("temperature", 20))
            post = WeatherUpdate(text, temp)
        else:
            print(f"Unknown post type: {post_type}")
            return

        post.publish()