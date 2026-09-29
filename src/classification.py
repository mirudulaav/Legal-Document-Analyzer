import re

CLAUSE_CATEGORIES = {
    "Definitions": [
        "means",
        "defined as",
        "definition",
        "for purposes of this agreement",
        "hereinafter"
    ],
    "Confidentiality": [
        "confidential",
        "confidential information",
        "non-disclosure",
        "disclose",
        "trade secret"
    ],
    "Termination": [
        "terminate",
        "termination",
        "notice of termination",
        "dismiss",
        "resign",
        "expiration"
    ],
    "Compensation": [
        "salary",
        "wages",
        "payment",
        "bonus",
        "compensation",
        "fee",
        "remuneration",
        "invoice"
    ],
    "Benefits": [
        "benefits",
        "insurance",
        "retirement",
        "vacation",
        "leave",
        "pension"
    ],
    "Intellectual Property": [
        "intellectual property",
        "copyright",
        "patent",
        "trademark",
        "invention",
        "work product",
        "license"
    ],
    "Liability": [
        "liability",
        "liable",
        "indemnity",
        "indemnification",
        "damages",
        "loss",
        "negligence"
    ],
    "Dispute Resolution": [
        "dispute",
        "arbitration",
        "arbitrator",
        "mediation",
        "court",
        "litigation"
    ],
    "Governing Law": [
        "governing law",
        "laws of",
        "jurisdiction",
        "applicable law"
    ],
    "Obligations": [
        "obligation",
        "responsibility",
        "duty"
    ],
    "Restrictions": [
        "non-compete",
        "non solicitation",
        "restriction",
        "prohibited",
        "shall not",
        "restrict"
    ],
    "General Provisions": [
        "entire agreement",
        "amendment",
        "severability",
        "waiver",
        "assignment",
        "notices"
    ],
    "Data Protection": [
        "personal data", "personal information", "data protection",
        "gdpr", "privacy policy", "data subject", "data controller"
    ],
    "Term": [
        "term of employment", "term of this agreement", "commence",
        "start date", "effective date", "duration"
    ],
    "Privacy": [
    "privacy","personal data","personal information","data processing","data protection",
    "data subject","data controller","data processor","cookie","cookies"
    ]
}


def classify_clause(clause_title, clause_content):
    title_text = clause_title.lower()
    body_text = clause_content.lower()

    scores = {}

    for category, keywords in CLAUSE_CATEGORIES.items():
        score = 0
        for keyword in keywords:
            pattern = r'\b' + re.escape(keyword) + r'\b'
            score += len(re.findall(pattern, title_text)) * 3   # title counts 3x
            score += len(re.findall(pattern, body_text))
        scores[category] = score

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return "Other"

    return best_category


def classify_clauses(clauses):
    results = []
    for clause in clauses:
        category = classify_clause(clause["title"], clause["content"])
        results.append({
            "section": clause["section"],
            "title": clause["title"],
            "category": category,
            "content": clause["content"],
        })
    return results