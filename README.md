# qa-risk-analyzer
Rule-based risk assessment engine for quality assurance workflows. Analyzes feature summaries against predefined security and functional testing criteria to recommend appropriate test strategies.

## Features
- Three-tier risk classification: High, Medium, Low
- Keyword-driven analysis: Pattern matching against security-critical flows (authentication, payments, integrations) and data validation
- Automated test recommendations: Contextual suggestions based on identified risk level
- FastAPI backend: RESTful API
- Test suite: 8 pytest tests covering risk classification, edge cases and validation

## Installation

### Prerequisites
- Python 3.12+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/ViviDickens/qa-risk-analyzer.git
cd qa-risk-analyzer

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the API

```bash
uvicorn app.main:app --reload
```

The server starts at http://localhost:8000.

### Health Check

```bash
curl http://localhost:8000/
```

Response:

```json
{"status": "ok"}
```

### Risk Analysis

Send a POST request to `/analyze-risk` with a feature summary:

```bash
curl -X POST "http://localhost:8000/analyze-risk" \
  -H "Content-Type: application/json" \
  -d '{"summary": "Login page with two-factor authentication"}'
```

Response example (High Risk):

```json
{
  "risk": "alto",
  "explanation": "The functionality includes critical flows such as authentication, payments, or backend integrations.",
  "recommended_tests": [
    "functional testing",
    "integration testing",
    "security testing"
  ]
}
```

## Classification Rules

### High Risk — Keywords: login, pago (payment), api
Includes authentication, payment processing, or API integrations.

### Medium Risk — Keywords: formulario (form), validación/validacion (validation)
User input and validation workflows.

### Low Risk — All other changes
Cosmetic or non-critical feature updates.

## Testing

Run the full test suite:

```bash
pytest tests/
```

Run with verbose output:

```bash
pytest tests/ -v
```

### Test Coverage
- `test_high_risk`: Validates High risk classification
- `test_medium_risk`: Validates Medium risk classification
- `test_low_risk`: Validates Low risk classification

All tests verify correct HTTP status codes (200) and risk level assignments.

## CI/CD

GitHub Actions workflow runs on every push/PR to main:
- Python 3.12 environment setup
- Dependency installation
- Flake8 linting (max complexity 10, line length 127)
- Pytest execution

## Project Structure

```text
qa-risk-analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application & routes
│   └── service.py       # Risk analysis logic
├── tests/
│   ├── __init__.py
│   └── test_risk.py     # Pytest test suite
├── .github/
│   └── workflows/
│       └── python-app.yml  # GitHub Actions CI/CD
├── requirements.txt
├── .gitignore
└── README.md
```

## Stack
- FastAPI — Modern async web framework
- Uvicorn — ASGI server
- pytest — Testing framework
- httpx — HTTP client for test requests

## Future Enhancements
- OWASP Top 10 2025 category mapping
- Machine learning–based keyword expansion
- Historical risk trend analysis
- Integration with Jira/test management tools

## License
MIT

Part of integrated QA automation portfolio (github.com/ViviDickens)
