from pathlib import Path

file_data = Path("Sample_Data/system.log")
target_words = ['error', 'warning', 'critical']

text = file_data.read_text().lower()

word_count = {}

for word in target_words:
    word_count[word] = text.count(word)

print(word_count)