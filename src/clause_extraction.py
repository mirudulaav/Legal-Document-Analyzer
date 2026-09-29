import re


TOP_LEVEL_PATTERNS = [
    r'(?im)^\s*(?:section|sec\.?)\s+(\d+)[\s.:\-]+(.+)$',
    r'(?im)^\s*article\s+([IVXLCDM]+|\d+)[\s.:\-]+(.+)$',
    r'(?m)^\s*(\d+)[.\s:\-]+([A-Z][A-Z0-9 ,&()/\-]{2,})\s*$',
    r'(?m)^\s*([IVXLCDM]+)[.\s:\-]+([A-Z][A-Z0-9 ,&()/\-]{2,})\s*$'
]

SUBCLAUSE_PATTERN = r'(?m)^\s*(\d+\.\d+(?:\.\d+)*)[\s.:\-]+(.+)$'


def find_matches(text, patterns):
    headings = []

    for pattern in patterns:
        for match in re.finditer(pattern, text):
            number = match.group(1).strip()
            title = match.group(2).strip()

            if len(title) > 150:
                continue

            headings.append({
                "start": match.start(),
                "number": number,
                "title": title
            })

    return headings


def extract_clauses(text):
    text = re.sub(r'\r\n', '\n', text)
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)

    top_level = find_matches(text, TOP_LEVEL_PATTERNS)
    sub_level = find_matches(text, [SUBCLAUSE_PATTERN])

    all_headings = top_level + sub_level

    all_headings.sort(key=lambda x: x["start"])

    unique = []
    seen = set()

    for heading in all_headings:
        if heading["start"] not in seen:
            unique.append(heading)
            seen.add(heading["start"])

    top_starts = {heading["start"] for heading in top_level}

    sections = []
    current = None

    for i, heading in enumerate(unique):

        if i + 1 < len(unique):
            end = unique[i + 1]["start"]
        else:
            end = len(text)

        content = text[heading["start"]:end].strip()

        lines = content.splitlines()

        if len(lines) > 1:
            body = " ".join(line.strip() for line in lines[1:])
        else:
            body = ""

        body = re.sub(r'\s+', ' ', body).strip()

        is_top = heading["start"] in top_starts
        top_number = heading["number"].split(".")[0]

        if is_top:

            current = {
                "section": heading["number"],
                "title": heading["title"],
                "content": body
            }

            sections.append(current)

        else:

            if (
                current is not None
                and current["section"].split(".")[0] == top_number
            ):

                joined = f"{heading['number']} {heading['title']} {body}".strip()

                current["content"] = (
                    current["content"] + " " + joined
                ).strip()

            else:

                sections.append({
                    "section": heading["number"],
                    "title": heading["title"],
                    "content": body
                })

    return sections