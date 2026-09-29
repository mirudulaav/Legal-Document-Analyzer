import pymupdf
import re


PAGE_MARKER = re.compile(
    r'^\s*Page\s+\d+\s*$',
    re.IGNORECASE
)


def extract_text_from_pdf(file_path):
    document = pymupdf.open(file_path)

    cleaned_pages = []

    for page in document:

        lines = page.get_text().splitlines()

        cleaned_lines = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if PAGE_MARKER.match(line):
                continue

            if "SAMPLE DOCUMENT - FICTIONAL, FOR NLP TESTING ONLY" in line:
                continue

            cleaned_lines.append(line)

        page_text = "\n".join(cleaned_lines)

        cleaned_pages.append(page_text)

    document.close()

    text = "\n".join(cleaned_pages)

    text = re.sub(r'\n+', '\n', text)

    return text.strip()