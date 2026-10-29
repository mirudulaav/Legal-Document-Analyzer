# Legal Document Analyzer

An NLP toolkit for analyzing text-based legal PDFs (employment agreements, leases, NDAs, service agreements, privacy policies, terms of service). It extracts and cleans text, splits a document into numbered clauses, produces an extractive summary, and measures similarity between documents. It uses classical NLP techniques (regex, TF-IDF, cosine similarity), so it needs no training data, LLM APIs, or GPU.

## Features

- **PDF text extraction**: reads text-based PDFs with PyMuPDF and strips page markers and repeated header/footer boilerplate.
- **Clause extraction**: detects `Section N`, `Article N/IV`, numbered ALL-CAPS headings (`1. TERMINATION`), Roman-numeral headings, and nested sub-clauses (`2.1`, `2.1.3`), then groups sub-clauses under their parent section.
- **Extractive summarization**: ranks sentences by TF-IDF cosine similarity to the document centroid and returns the top N in original order.
- **Document similarity**: returns a TF-IDF cosine similarity score between two documents as a percentage.
- **Text preprocessing**: lowercasing, tokenization and stop-word removal, keeping legally meaningful negations and conditions (`not`, `no`, `nor`, `under`, `unless`).

## Project Structure

```
Legal-Document-Analyzer/
├── data/
│   └── documents/            # input legal PDFs
├── src/
│   ├── clause_extraction.py  # text -> list of sections/clauses
│   ├── pdf_extractor.py      # PDF -> clean text
│   ├── preprocessing.py      # normalization, tokenization, stop-word removal
│   ├── similarity.py         # TF-IDF cosine similarity between two texts
│   └── summarization.py      # TF-IDF extractive summarizer
├── app.py                    # application entry point
├── requirements.txt          # Python dependencies
└── .gitignore
```

## Requirements

- Python 3.9+
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [NLTK](https://www.nltk.org/)
- [scikit-learn](https://scikit-learn.org/)

## Installation

```bash
python -m venv venv
venv\Scripts\activate         # Windows (use: source venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

## Usage

Run from the project root so `src` is importable.

### Extract text from a PDF

```python
from src.pdf_extractor import extract_text_from_pdf

text = extract_text_from_pdf("data/documents/nda.pdf")
```

### Extract clauses

```python
from src.clause_extraction import extract_clauses

clauses = extract_clauses(text)
for c in clauses:
    print(c["section"], c["title"])
    print(c["content"][:200])
```

Each clause is a dict:

```python
{"section": "2", "title": "TERM AND TERMINATION", "content": "..."}
```

### Summarize

```python
from src.summarization import summarize_text

summary = summarize_text(text, num_sentences=8)
```

### Compare two documents

```python
from src.similarity import calculate_similarity

score = calculate_similarity(text_a, text_b)  # e.g. 63.27 (percent)
```

### Preprocess text

```python
from src.preprocessing import preprocess_text

tokens = preprocess_text(text)  # space-joined, lowercased, stop words removed
```

## Module Reference

| Module | Function | Description |
|---|---|---|
| `pdf_extractor` | `extract_text_from_pdf(file_path)` | Returns cleaned text from all pages of a PDF. |
| `preprocessing` | `preprocess_text(text)` | Splits camelCase joins, tokenizes, lowercases, removes stop words. |
| `clause_extraction` | `extract_clauses(text)` | Returns a list of `{section, title, content}` dicts. |
| `summarization` | `split_sentences(text)` | Sentence splitter that drops short and boilerplate lines. |
| `summarization` | `summarize_text(text, num_sentences=8)` | Top-N centroid-ranked sentences, in document order. |
| `similarity` | `calculate_similarity(text1, text2)` | Cosine similarity of TF-IDF vectors, as a percentage (0-100). |

## Limitations

- Works on **text-based PDFs only**; scanned documents need OCR first.
- `pdf_extractor` removes a specific test-document footer (`SAMPLE DOCUMENT - FICTIONAL, FOR NLP TESTING ONLY`) and `Page N` lines. Adjust these filters for other documents.
- Clause detection is regex-based and tuned to common numbering styles; unusual formats may be missed or split incorrectly.
- Summarization is extractive, so it selects existing sentences rather than rewriting them.
- Similarity is lexical (TF-IDF), not semantic, so it will not catch paraphrases.

## Roadmap

- Named entity recognition (parties, dates, amounts)
- Clause classification (termination, confidentiality, liability, etc.)
- A UI or CLI entry point

## License

Add a license of your choice (e.g. MIT).
