import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_sentences(text):
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)

    cleaned = []
    for sentence in sentences:
        s = sentence.strip()
        if len(s) <= 30:
            continue
        # drop repeated page header/footer boilerplate
        if re.search(r'SAMPLE DOCUMENT|Page \d+', s, re.IGNORECASE):
            continue
        cleaned.append(s)
    return cleaned

def summarize_text(text, num_sentences=8):
    sentences = split_sentences(text)

    if len(sentences) <= num_sentences:
        return " ".join(sentences)

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(sentences)

    document_vector = matrix.toarray().mean(axis=0, keepdims=True)

    scores = cosine_similarity(matrix, document_vector).flatten()

    ranked_indices = scores.argsort()[-num_sentences:]
    ranked_indices = sorted(ranked_indices)

    summary = [sentences[i] for i in ranked_indices]
    return " ".join(summary)

