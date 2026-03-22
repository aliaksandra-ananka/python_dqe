import os
import xml.etree.ElementTree as ET

from .news import News
from .private_ad import PrivateAd
from .weather import WeatherUpdate
from utils.text_utils import normalize_text, fix_iz_mistakes


class XMLProcessingError(Exception):
    """Custom exception for XML processing"""
    pass


class XMLPostProvider:
    """Read posts from XML file and publish them"""

    def __init__(self, file_path=None):
        self.file_path = file_path or os.path.join("input", "posts.xml")

    def process_file(self):
        # ---- check file exists ----
        if not os.path.exists(self.file_path):
            raise XMLProcessingError(f"File not found: {self.file_path}")

        try:
            tree = ET.parse(self.file_path)  # read XML file
            root = tree.getroot()  # get root element <posts>
        except Exception as e:
            raise XMLProcessingError(f"Error parsing XML: {e}")

        # ---- iterate over all <post> elements ----
        for post_element in root.findall("post"):
            self._process_post(post_element)

        # ---- delete file after successful processing ----
        os.remove(self.file_path)
        print(f"File {self.file_path} processed and deleted.")

    def _process_post(self, element):
        """Convert XML element into Post object"""

        post_type = element.get("type", "").lower()  # attribute type="News"

        # extract child elements safely
        text = self._get_text(element, "text")

        # normalize text (reuse previous homework logic)
        text = fix_iz_mistakes(normalize_text(text))

        if post_type == "news":
            city = self._get_text(element, "city", default="Unknown")
            post = News(text, city)

        elif post_type == "privatead":
            expiration = self._get_text(element, "expiration")
            post = PrivateAd(text, expiration)

        elif post_type == "weather":
            temp = int(self._get_text(element, "temperature", default="20"))
            post = WeatherUpdate(text, temp)

        else:
            print(f"Unknown post type: {post_type}")
            return

        post.publish()

    @staticmethod
    def _get_text(parent, tag, default=""):
        """Helper to safely extract text from XML element"""
        el = parent.find(tag)
        return el.text.strip() if el is not None and el.text else default