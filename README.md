# Django TF-IDF Analyzer 📊

A simple Django project that lets users upload a `.txt` file and analyzes the Term Frequency and Inverse Document Frequency (TF-IDF) of words in the text.

## Features
- Upload `.txt` files up to 5MB
- Handles different text encodings with `chardet`
- Displays top 50 words sorted by TF-IDF
- Clean UI with error handling

## Setup
```bash
pip install -r requirements.txt
python manage.py runserver
