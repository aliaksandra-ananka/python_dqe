import random
import string
import re
import copy  # для демонстрации shallow/deep copy

# ------------------------------
# Module 2 homework: random dicts
# ------------------------------

def generate_random_dict(num_keys=5, key_source=string.ascii_lowercase, value_range=(0, 100)):
    """
    Generate a random dict with letters as keys and random integers as values.
    Parameters:
        num_keys (int): number of keys in the dict
        key_source (str): string of possible letters for keys
        value_range (tuple): min and max values for numbers
    Returns:
        dict: generated random dict
    """
    keys = random.sample(key_source, num_keys)  # pick unique letters
    return {k: random.randint(*value_range) for k in keys}  # dict comprehension

def generate_list_of_dicts(num_dicts=5, **kwargs):
    """Generate a list of random dicts."""
    return [generate_random_dict(**kwargs) for _ in range(num_dicts)]

def combine_dicts(dict_list):
    """
    Combine list of dicts into one dict:
    - If key occurs in multiple dicts, take max value and rename key with dict index.
    - If key occurs once, take as is.
    """
    key_sources = {}
    for idx, d in enumerate(dict_list, start=1):
        for k, v in d.items():
            key_sources.setdefault(k, []).append((v, idx))  # store list of (value, dict_index)

    combined = {}
    for k, values in key_sources.items():
        if len(values) == 1:
            combined[k] = values[0][0]
        else:
            max_val, max_idx = max(values, key=lambda x: x[0])
            combined[f"{k}_{max_idx}"] = max_val
    return combined

# ------------------------------
# Module 3 homework: string normalization
# ------------------------------

def normalize_text(text):
    """Normalize text to lowercase."""
    return text.lower()

def fix_iz_mistakes(text):
    """Replace 'iZ' with 'is' only when it's a mistake (whole word)."""
    return re.sub(r'\biZ\b', 'is', text, flags=re.IGNORECASE)

def extract_last_words_sentence(text):
    """Create a new sentence using last words of each existing sentence."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    last_words = [s.strip().split()[-1].strip(".!?") for s in sentences if s.strip()]
    return " ".join(last_words).capitalize() + "."

def append_sentence(text, sentence):
    """Append a sentence to the end of text."""
    return text + " " + sentence

def count_whitespaces(text):
    """Count all whitespace characters in text."""
    return sum(1 for c in text if c.isspace())

# ------------------------------
# Functional approach: execution
# ------------------------------

def run_module2_example(num_dicts=3, **kwargs):
    """Generate random dicts, combine them, and return results."""
    dict_list = generate_list_of_dicts(num_dicts=num_dicts, **kwargs)
    combined_dict = combine_dicts(dict_list)
    return dict_list, combined_dict

def run_module3_example(text):
    """Normalize text, fix mistakes, add sentence, count whitespaces."""
    normalized = normalize_text(text)
    fixed = fix_iz_mistakes(normalized)
    new_sentence = extract_last_words_sentence(fixed)
    final_text = append_sentence(fixed, new_sentence)
    whitespace_count = count_whitespaces(final_text)
    return final_text, whitespace_count

# ------------------------------
# Examples / Usage
# ------------------------------

# Module 2 execution
dicts_list, combined = run_module2_example(num_dicts=4, num_keys=3)
print("Module 2 - list of dicts:", dicts_list)
print("Module 2 - combined dict:", combined)

# Module 3 execution
text_example = """tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

final_text, ws_count = run_module3_example(text_example)
print("\nModule 3 - normalized text:\n", final_text)
print("Module 3 - whitespace count:", ws_count)

# ------------------------------
# Optional: demonstrate shallow and deep copy
# ------------------------------
combined_shallow = copy.copy(combined)  # shallow copy
combined_deep = copy.deepcopy(combined)  # deep copy