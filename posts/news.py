from .base import Post
from datetime import datetime

class News(Post):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def _format(self):
        return f"News ----------------\n{self._text}\nCity: {self.city}, Date: {self.date}"