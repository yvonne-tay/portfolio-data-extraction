# portfolio-data-extraction

A sanitized, end-to-end example of a portfolio data extraction and transformation workflow, designed to demonstrate how data pipelines are structured, documented, and delivered in an enterprise setting.

This repository is intentionally simplified and anonymised to focus on workflow design, reproducibility, and clarity rather than proprietary implementation details.

---

## What this project demonstrates

- Translating a business data requirement into a technical workflow
- Structuring a repeatable data extraction and transformation pipeline
- Using Python and pandas for data processing
- Designing scripts that are configurable via CLI arguments
- Handling enterprise constraints such as security and data sanitisation

---

## Project structure & Quickstart

```text
portfolio-data-extraction/
├─ src/
│  ├─ extract_portfolio_data.py   # Main data extraction + transformation script
│  └─ sample_data/
│     └─ sample_output.csv        # Sample output (dummy data)
├─ requirements.txt               # Python dependencies
├─ README.md
└─ .gitignore

# Quickstart

# 1) Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the script
python src/extract_portfolio_data.py \
  --nodes CCORP HCORP \
  --out src/sample_data/sample_output.csv
