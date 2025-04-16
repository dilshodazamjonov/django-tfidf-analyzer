import re
import chardet
from collections import Counter
from math import log
from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(file):
    # Detect encoding
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'

    try:
        text = raw_data.decode(encoding)
    except UnicodeDecodeError:
        raise ValueError("The file is not a valid text file or has unsupported encoding.")

    if not text.strip():
        raise ValueError("Uploaded file is empty.")

    # Split text into pseudo-documents using sentences
    sentences = re.split(r'[.!?]+\s*', text.strip())
    total_docs = len(sentences)

    # Document Frequency (DF): in how many sentences each word appears
    word_doc_freq = Counter()
    for sentence in sentences:
        unique_words = set(re.findall(r'\b[а-яА-ЯёЁa-zA-Z\-]+\b', sentence.lower()))
        for word in unique_words:
            word_doc_freq[word] += 1

    # Term Frequency (TF): count words in the full document

    all_words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z\-]+\b', text.lower())
    tf = Counter(all_words)

    idf = {
        word: log(total_docs / word_doc_freq[word])
        for word in tf
    }

    result = [
        {"word": word, "tf": tf[word], "idf": round(idf[word], 3)}
        for word in tf
    ]

    result.sort(key=lambda x: x["idf"], reverse=True)
    return result[:50]


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            # Check file extension
            if not uploaded_file.name.endswith('.txt'):
                return render(request, 'tf/upload.html', {
                    'form': form,
                    'error': 'Only .txt files are allowed.'
                })

            # Limit file size (max 5MB)
            if uploaded_file.size > 5 * 1024 * 1024:
                return render(request, 'tf/upload.html', {
                    'form': form,
                    'error': 'File is too large. Max 5MB allowed.'
                })

            try:
                data = handle_uploaded_file(uploaded_file)
                return render(request, 'tf/result.html', {'data': data})
            except Exception as e:
                return render(request, 'tf/upload.html', {
                    'form': form,
                    'error': f'Error processing file: {str(e)}'
                })
    else:
        form = UploadFileForm()
    return render(request, 'tf/upload.html', {'form': form})

