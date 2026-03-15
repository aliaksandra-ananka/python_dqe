from datetime import datetime, date
import os

# ------------------------------
# Base class for a Post
# ------------------------------

class Post:
    _file_path = "news_feed.txt"  # class variable: file to store all posts

    def __init__(self, text):
        self._text = text  # private instance variable for content

    def publish(self):
        """Publish record to file. Calls internal format method."""
        formatted_text = self._format()
        with open(Post._file_path, "a", encoding="utf-8") as f:
            f.write(formatted_text + "\n\n")
        print("Record published!")

    def _format(self):
        """Private method to format the post. Override in child classes."""
        raise NotImplementedError("Subclasses must implement _format method")

# ------------------------------
# News class
# ------------------------------

class News(Post):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")  # instance variable: publish date

    def _format(self):
        """Format News for file"""
        return f"News ----------------\n{self._text}\nCity: {self.city}, Date: {self.date}"

# ------------------------------
# PrivateAd class
# ------------------------------

class PrivateAd(Post):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()

    @property
    def days_left(self):
        """Calculate remaining days for ad"""
        delta = self.expiration_date - date.today()
        return delta.days if delta.days > 0 else 0

    def _format(self):
        """Format PrivateAd for file"""
        return f"Private Ad -------------\n{self._text}\nExpires in {self.days_left} day(s)"

# ------------------------------
# Unique Post type: WeatherUpdate
# ------------------------------

class WeatherUpdate(Post):
    def __init__(self, text, temperature):
        super().__init__(text)
        self.temperature = temperature  # integer temperature in Celsius

    @staticmethod
    def temperature_state(temp):
        """Return description based on temperature"""
        if temp < 10:
            return "cold"
        elif 10 <= temp < 25:
            return "warm"
        else:
            return "hot"

    def _format(self):
        """Format WeatherUpdate for file"""
        state = WeatherUpdate.temperature_state(self.temperature)
        return f"Weather Update ----------\n{self._text}\nTemperature: {self.temperature}°C ({state})"

# ------------------------------
# Function to add a post interactively
# ------------------------------

def add_post():
    print("Select post type:\n1 - News\n2 - Private Ad\n3 - Weather Update")
    choice = input("Enter number: ").strip()
    if choice == "1":
        text = input("Enter news text: ").strip()
        city = input("Enter city: ").strip()
        post = News(text, city)
    elif choice == "2":
        text = input("Enter ad text: ").strip()
        exp_date = input("Enter expiration date (YYYY-MM-DD): ").strip()
        post = PrivateAd(text, exp_date)
    elif choice == "3":
        text = input("Enter weather update text: ").strip()
        temp = int(input("Enter temperature (°C): ").strip())
        post = WeatherUpdate(text, temp)
    else:
        print("Invalid choice!")
        return

    post.publish()

# ------------------------------
# Main interactive loop
# ------------------------------

if __name__ == "__main__":
    while True:
        add_post()
        cont = input("Add another post? (y/n): ").strip().lower()
        if cont != "y":
            break
    print("All done! Check news_feed.txt for results.")