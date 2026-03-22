from .base import Post
from datetime import datetime
from database.db_manager import DatabaseManager


class News(Post):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def _format(self):
        return f"News ----------------\n{self._text}\nCity: {self.city}, Date: {self.date}"

    def publish(self):
        super().publish()

        db = DatabaseManager()
        db.insert_news(self._text, self.city, self.date)
        db.close()