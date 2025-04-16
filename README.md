# Django TF-IDF Analyzer

A simple Django project that lets users upload a `.txt` file and analyzes the Term Frequency and Inverse Document Frequency (TF-IDF) of words in the text.

## Features

- Upload `.txt` files up to 5MB
- Handles different text encodings with `chardet`
- Displays top 50 words sorted by TF-IDF
- Clean UI with error handling

## Setup

To run this project locally, follow these steps:

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/yourusername/django-tfidf-analyzer.git
cd django-tfidf-analyzer


# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


