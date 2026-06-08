# ForensiX

ForensiX - Digital Forensics Analyzer

ForensiX collects file system metadata and deep file-type metadata using ExifTool plus specialized parsers for PDF, Office, audio, images, and more. It generates an Excel evidence report and flags suspicious indicators.

## Features

- Recursive file discovery
- General metadata extraction via ExifTool
- Specialized metadata extraction: PDF, DOCX, audio, images (extendable)
- Hashing (MD5, SHA1, SHA256)
- Suspicious indicators analyzer
- Excel report generator (`output/forensix_report.xlsx`)

## Prerequisites

- Python 3.8+ (recommended)
- ExifTool (external executable) installed and available or path set in `config.py` as `EXIFTOOL_PATH`
- Create and activate a virtual environment and install Python dependencies

## Quick setup

Install these libraries to get start - 
pip install pandas openpyxl pyexiftool python-docx pypdf2 mutagen pefile tqdm oletools

Note : Some user might need to create virtual python environment


## Usage

Set the source folder in `config.py` (default `test_data`) and the `EXIFTOOL_PATH` if ExifTool is not on your PATH.

Run the tool:

```bash
.\.venv\Scripts\python main.py
```

Output Excel report will be written to `output/forensix_report.xlsx`.

## Files of Interest

- `main.py` — entry point
- `collectors/` — specialized and generic collectors
- `analysers/` — analysis logic (suspicious indicators)
- `normalizers/` — normalization layer
- `routers/` — file-type routing
- `reports/` — Excel report generator
- `utils/` — helper utilities (hashing, discovery)

## Repository Description (one-line)

ForensiX — Extracts and correlates file metadata using ExifTool and specialized parsers to produce forensic-quality reports.

## Suggested GitHub repository content

- `README.md` (this file)
- `.gitignore` (ignore venv, outputs, secrets)
- `main.py`
- `collectors/`, `analysers/`, `routers/`, `normalizers/`, `reports/`, `utils/`
- `test_data/` (example files, do NOT commit sensitive evidence)
- `requirements.txt` (pin your dependencies)

## License

MIT
