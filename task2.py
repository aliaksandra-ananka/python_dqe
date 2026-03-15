import re  # import regular expressions module

# ---- Step 1: copy the text to a variable ----
text = """tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# ---- Step 2: normalize letter cases ----
text_normalized = text.lower()  # convert all letters to lowercase

# ---- Step 3: fix the specific mistake "iZ" -> "is" ONLY if it is a mistake ----
# Using regex with word boundaries to avoid replacing legitimate "iz" in words
text_fixed = re.sub(r'\biZ\b', 'is', text_normalized, flags=re.IGNORECASE)

# ---- Step 4: create one more sentence with the last words of each existing sentence ----
# Split text into sentences using regex (consider '.', '?', '!')
sentences = re.split(r'(?<=[.!?])\s+', text_fixed)  # split on punctuation followed by whitespace

last_words = []  # list to store last words
for s in sentences:
    words = s.strip().split()  # split sentence into words
    if words:  # avoid empty sentences
        last_words.append(words[-1].strip(".!?"))  # take last word and remove punctuation

# Join last words into one sentence
new_sentence = " ".join(last_words).capitalize() + "."  # capitalize first letter

# ---- Step 5: append new sentence to the end of text ----
final_text = text_fixed + " " + new_sentence

# ---- Step 6: count all whitespace characters ----
whitespace_count = sum(1 for c in final_text if c.isspace())  # counts spaces, tabs, newlines, etc.

# ---- Step 7: print results ----
print("Normalized and fixed text:\n")
print(final_text)
print("\nNumber of whitespace characters:", whitespace_count)