import re
import unicodedata


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _has_any(text: str, patterns: list) -> bool:
    return any(re.search(p, text) for p in patterns)


HIGH_PATTERNS = [r"\blogin\b", r"\bpagos?\b", r"\bpayments?\b", r"\bapis?\b"]
MEDIUM_PATTERNS = [
    r"\bformularios?\b",
    r"\bforms?\b",
    r"\bvalidacion(es)?\b",
    r"\bvalidations?\b",
]


def analyze_risk(text: str) -> dict:
    normalized_text = _normalize(text)

    if _has_any(normalized_text, HIGH_PATTERNS):
        return {
            "risk": "alto",
            "explanation": "The functionality includes critical flows such as authentication, payments, or backend integrations.",
            "recommended_tests": [
                "functional testing",
                "integration testing",
                "security testing"
            ]
        }

    if _has_any(normalized_text, MEDIUM_PATTERNS):
        return {
            "risk": "medio",
            "explanation": "The functionality includes validations or user input flows with moderate impact.",
            "recommended_tests": [
                "functional testing",
                "validation testing",
                "UI testing"
            ]
        }

    return {
        "risk": "bajo",
        "explanation": "The change appears limited and does not suggest a critical impact.",
        "recommended_tests": [
            "smoke testing",
            "basic functional testing"
        ]
    }
