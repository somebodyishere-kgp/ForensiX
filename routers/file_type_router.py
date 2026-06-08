from pathlib import Path

def get_file_type(file_path):
    extension = Path(
        file_path
    ).suffix.lower()

    mapping = {
        ".pdf": "pdf",

        ".docx": "docx",

        ".xlsx": "office",

        ".pptx": "office",

        ".mp3": "audio",

        ".wav": "audio",

        ".flac": "audio",

        ".jpg": "image",

        ".jpeg": "image",

        ".png": "image",

        ".mp4": "video",

        ".mov": "video",

        ".doc": "office",

        ".ppt": "office",

        ".exe": "executable",

        ".zip": "archive",

        ".txt": "text",

        ".rtf": "document",

        ".7z": "archive",
        
        ".rar": "archive",
    }

    return mapping.get(
        extension,
        "generic"
    )