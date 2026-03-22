from .base import Post
from database.db_manager import DatabaseManager


class WeatherUpdate(Post):
    def __init__(self, text, temperature):
        super().__init__(text)
        self.temperature = temperature

    def _format(self):
        return f"Weather Update ----------\n{self._text}\nTemperature: {self.temperature}"

    def publish(self):
        super().publish()

        db = DatabaseManager()
        db.insert_weather(self._text, self.temperature)
        db.close()