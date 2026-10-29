import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english")) - {"not", "no", "nor", "under", "unless"}

def preprocess_text(text):
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)
