def analyze_risk(text: str) -> dict:
    normalized_text = text.lower()

    if (
        "login" in normalized_text
        or "pago" in normalized_text
        or "api" in normalized_text
    ):
        return {
            "risk": "alto",
            "explanation": "The functionality includes critical flows such as authentication, payments, or backend integrations.",
            "recommended_tests": [
                "functional testing",
                "integration testing",
                "security testing"
            ]
        }

    if (
        "formulario" in normalized_text
        or "validación" in normalized_text
        or "validacion" in normalized_text
    ):
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