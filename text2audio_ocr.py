# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:27:15 2023

@author: mgalaval
"""
import re
from gtts import gTTS
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

# Function to remove special characters and leading/trailing whitespace
def clean_text(text):
    # Replace all non-alphanumeric characters (excluding space) with an empty string
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    # Remove leading and trailing whitespace
    cleaned_text = cleaned_text.strip()

    return cleaned_text

# Function to convert text to audio using gTTS
def text_to_audio(text, lang, output_audio_path):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_audio_path)


# Replace the image path with the path to your image file
image_path = r"..\subtitle-of-a-blu-ray-movie.jpg"
output_text_path = r"..\output_text.txt"
output_audio_path = r"..\output_audio.mp4"

# Extract text from the image and clean it
extracted_text = extract_text_from_image(image_path)
cleaned_text = clean_text(extracted_text)

# Save the cleaned text to a text file
with open(output_text_path, "w") as text_file:
    text_file.write(cleaned_text)

# Define the language code for english for german change it to "de"
language_code = "en"

# Convert cleaned text to audio in German and save it as an MP3 file
text_to_audio(cleaned_text, language_code, output_audio_path)