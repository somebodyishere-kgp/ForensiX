"""
ForensiX Configuration File
"""

import os
from pathlib import Path

# directories
PROJECT_ROOT = Path(__file__).parent

INPUT_DIRECTORY = "test_data"  # Where to scan for files
OUTPUT_DIRECTORY = PROJECT_ROOT / "output"  # Where to save reports

# create out dir if it doesn't exist
OUTPUT_DIRECTORY.mkdir(exist_ok=True)

# file types
SUPPORTED_EXTENSIONS = {
    # Images
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp",
    
    # Documents
    ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt",
    
    # Audio
    ".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg",
    
    # Video
    ".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv",
    
    # Archives
    ".zip", ".rar", ".7z", ".tar", ".gz",
    
    # Executables & Code
    ".exe", ".dll", ".bat", ".ps1", ".py", ".js",
    
    # Text
    ".txt", ".rtf", ".log", ".csv", ".json", ".xml",
}

# suspicious
REVISION_COUNT_THRESHOLD = 100  # Flag if document has > 100 revisions

# report setting
EXCEL_REPORT_NAME = "forensix_report.xlsx"
INCLUDE_RAW_METADATA = False  # true to include massive raw_metadata in Excel

# loggin
DEBUG_MODE = False  # true for verbose output

#path to exiftool
EXIFTOOL_PATH = r"C:\exiftool\exiftool.exe"  

# helper fxn
def get_output_path(filename):
    """Get full path for output file"""
    return OUTPUT_DIRECTORY / filename

def is_supported_file(file_path):
    """Check if file extension is supported"""
    ext = Path(file_path).suffix.lower()
    return ext in SUPPORTED_EXTENSIONS