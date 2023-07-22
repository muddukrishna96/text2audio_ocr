# text2audio_ocr

This repository contains Python code to extract text from an image using Optical Character Recognition (OCR), clean the extracted text by removing special characters, and generate  text-to-speech (TTS) using gTTS.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Requirements

- Python 3.x
- Tesseract OCR (for text extraction)
- pytesseract library
- gTTS library with the German language package

## Installation

1. Install Python 3.x if you don't have it already: [Python Downloads](https://www.python.org/downloads/)

2. Install Tesseract OCR:
   - On macOS: `brew install tesseract`
   - On Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - On Windows: Download the installer from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and follow the instructions.

3. Install Python libraries:
   pip install pytesseract gTTS gtts-token

Example
Suppose you have an image named "example.png" with english text. After running the script, the extracted text will be saved in "output_text.txt," and the generated German/english or any audio of your choice audio will be saved in "output_audio.mp3."



# The extracted and cleaned  text will be here
The content of "output_text.txt" 
You can listen to the generated German audio by playing the "output_audio.mp3" file.

#Caution 
This code provide a simple use case of text to speech conversion .For further understanding of ocr used in the code refer https://github.com/UB-Mannheim/tesseract
