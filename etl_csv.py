import csv
from collections import Counter
from utils.text_utils import normalize_text, fix_iz_mistakes

INPUT_FILE = "news_feed.txt"
WORD_CSV = "word_count.csv"
LETTER_CSV = "letter_count.csv"

def read_text_file(file_path):
    """Read the content of the text file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return ""

def preprocess_text(text):
    """Apply lowercase normalization and fix iZ mistakes"""
    text = fix_iz_mistakes(text)
    text = normalize_text(text)
    return text

def count_words(text):
    """Return dictionary with word counts"""
    words = [w.strip(".,!?;:()\"") for w in text.split()]
    counter = Counter(words)
    return counter

def count_letters(text):
    """Return dictionary with counts per letter, uppercase counts, and percentage"""
    letters_only = [c for c in text if c.isalpha()]
    counter_all = Counter(letters_only)
    counter_upper = Counter(c for c in letters_only if c.isupper())
    result = []
    for letter in sorted(counter_all):
        total = counter_all[letter]
        upper = counter_upper.get(letter, 0)
        percent = round(upper / total * 100, 2)
        result.append({
            "letter": letter.lower(),
            "count_all": total,
            "count_uppercase": upper,
            "percentage": percent
        })
    return result

def write_word_csv(word_counter, file_path):
    """Write word count CSV"""
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in sorted(word_counter.items()):
            writer.writerow([word, count])

def write_letter_csv(letter_stats, file_path):
    """Write letter count CSV"""
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["letter", "count_all", "count_uppercase", "percentage"])
        writer.writeheader()
        for row in letter_stats:
            writer.writerow(row)

if __name__ == "__main__":
    text = read_text_file(INPUT_FILE)
    preprocessed = preprocess_text(text)

    # word counts
    word_counter = count_words(preprocessed)
    write_word_csv(word_counter, WORD_CSV)

    # letter counts
    letter_stats = count_letters(text)  # используем оригинальный текст для учета верхнего регистра
    write_letter_csv(letter_stats, LETTER_CSV)

    print(f"CSV files '{WORD_CSV}' and '{LETTER_CSV}' have been created/updated.")