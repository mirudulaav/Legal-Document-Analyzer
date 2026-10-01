# Legal Document Analyzer

A Natural Language Processing application that analyzes legal documents and extracts useful information from their content.

The application allows users to upload legal PDF documents and performs clause extraction, clause classification, extractive summarization, and document similarity analysis.

## Features

* Upload legal PDF documents
* Extract text from PDF files
* Preprocess extracted text
* Extract legal clauses and sections
* Classify clauses into legal categories
* Generate an extractive summary
* Compare two legal documents using text similarity
* Interactive Streamlit web interface

## NLP Techniques

### 1. Text Preprocessing

The extracted document text is cleaned and prepared for NLP processing using:

* Text normalization
* Tokenization
* Stopword removal
* Regular expression based cleaning

### 2. Clause Extraction

The system identifies sections and clauses from legal documents using pattern-based text processing.

It can detect formats such as:

* `1. Section Title`
* `Section 1: Section Title`
* `Article I: Section Title`
* Subclauses such as `1.1`, `1.2`, and `1.3`

### 3. Clause Classification

Extracted clauses are classified into legal categories using keyword-based classification.

Supported categories include:

* Definitions
* Confidentiality
* Termination
* Compensation
* Benefits
* Intellectual Property
* Liability
* Dispute Resolution
* Governing Law
* Obligations
* Restrictions
* General Provisions
* Data Protection
* Term
* Other

### 4. Extractive Summarization

The application uses **TF-IDF** to identify important sentences from the document.

The most relevant sentences are selected to create a concise summary while preserving the original wording of the document.

### 5. Document Similarity

Two legal documents can be compared using:

* TF-IDF vectorization
* Cosine similarity

The system returns a similarity percentage based on textual similarity.

The similarity score does not determine legal equivalence or legal validity.

## Technologies Used

* Python
* Streamlit
* PyMuPDF
* NLTK
* Scikit-learn
* NumPy
* Regular Expressions

## Project Structure

```text
Legal-Document-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── pdf_extractor.py
    ├── preprocessing.py
    ├── clause_extraction.py
    ├── classification.py
    ├── summarization.py
    └── similarity.py
```

## Application Workflow

```text
Legal PDF
    ↓
PDF Text Extraction
    ↓
Text Preprocessing
    ↓
Clause Extraction
    ↓
Clause Classification
    ↓
TF-IDF Summarization
    ↓
TF-IDF + Cosine Similarity
    ↓
Streamlit Interface
```


## Usage

1. Open the application.
2. Upload a legal PDF.
3. View the extracted document text.
4. View the detected legal clauses.
5. View the classification of each clause.
6. View the generated document summary.
7. Upload a second legal PDF to calculate textual similarity.

## Supported Documents

The application can be used with different types of text-based legal documents, including:

* Employment agreements
* Terms of service
* Non-disclosure agreements
* Lease agreements
* Privacy policies
* Service agreements
* Other structured legal documents

The quality of extraction depends on the PDF containing selectable text. Scanned image-only PDFs may require OCR before analysis.


## Limitations

* Clause classification is keyword-based.
* Summarization is extractive rather than generative.
* Similarity measures textual similarity and does not determine legal equivalence.
* Scanned PDFs without a text layer may not be processed correctly.
* The application is an NLP analysis tool and does not provide legal advice.
