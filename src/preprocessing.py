import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9.,;:%$()'-]", " ", text)

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)