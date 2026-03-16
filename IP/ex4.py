from googletrans import Translator

# Create translator object
translator = Translator()

# Input text
text = input("Enter text to translate: ")

# Source and destination languages
source_lang = input("Enter source language (e.g., en): ")
target_lang = input("Enter target language (e.g., fr): ")

# Perform translation
translated = translator.translate(text, src=source_lang, dest=target_lang)

# Display result
print("Original Text:", text)
print("Translated Text:", translated.text)