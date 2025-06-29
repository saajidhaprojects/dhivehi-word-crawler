
import os
import re
from dhivehi_detector import is_dhivehi

class WordProcessor:
    def __init__(self, storage_location):
        self.storage_location = storage_location
        self.word_count = 0
        os.makedirs(self.storage_location, exist_ok=True)

    def process_text(self, text):
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            if is_dhivehi(word):
                self.save_word(word)

    def save_word(self, word):
        self.word_count += 1

        if self.word_count % 1000 == 1 and self.word_count != 1:
            new_location = input(f"\nCollected {self.word_count - 1} words.\nEnter new storage folder path:\n")
            if os.path.isdir(new_location):
                self.storage_location = new_location
            else:
                print("Invalid path. Continuing with previous folder.")

        safe_word = word.replace(" ", "_")
        filename = os.path.join(self.storage_location, f"{self.word_count}_{safe_word}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(word)
        print(f"Saved word: {word}")
