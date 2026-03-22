from .base import Post

class WeatherUpdate(Post):
    def __init__(self, text, temperature):
        super().__init__(text)
        self.temperature = temperature

    @staticmethod
    def temperature_state(temp):
        if temp < 10:
            return "cold"
        elif 10 <= temp < 25:
            return "warm"
        else:
            return "hot"

    def _format(self):
        state = WeatherUpdate.temperature_state(self.temperature)
        return f"Weather Update ----------\n{self._text}\nTemperature: {self.temperature}°C ({state})"