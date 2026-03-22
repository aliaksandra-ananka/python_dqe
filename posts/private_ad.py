from .base import Post
from datetime import datetime, date

class PrivateAd(Post):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

    @property
    def days_left(self):
        delta = self.expiration_date - date.today()
        return delta.days if delta.days > 0 else 0

    def _format(self):
        return f"Private Ad -------------\n{self._text}\nExpires in {self.days_left} day(s)"
