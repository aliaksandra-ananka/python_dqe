import re

def normalize_text(text: str) -> str:
    """Convert all letters to lowercase."""
    return text.lower()

def fix_iz_mistakes(text: str) -> str:
    """Replace 'iZ' with 'is' only when it is a mistake (whole word)."""
    return re.sub(r'\biZ\b', 'is', text, flags=re.IGNORECASE)