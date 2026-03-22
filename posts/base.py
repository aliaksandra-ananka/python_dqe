from datetime import datetime

class Post:
    _file_path = "news_feed.txt"

    def __init__(self, text):
        self._text = text

    def publish(self):
        formatted_text = self._format()
        with open(Post._file_path, "a", encoding="utf-8") as f:
            f.write(formatted_text + "\n\n")
        print("Record published!")

    def _format(self):
        raise NotImplementedError("Subclasses must implement _format method")