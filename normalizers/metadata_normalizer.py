def _sanitize_key(k):
    return k.replace(":", "_").replace(" ", "_")

def normalize_metadata(metadata):
    normalized = {
        "filename": metadata.get("File:FileName"),
        "directory": metadata.get("File:Directory"),
        "file_size": metadata.get("File:FileSize"),
        "mime_type": metadata.get("File:MIMEType"),
        "created": metadata.get("File:FileCreateDate"),
        "modified": metadata.get("File:FileModifyDate"),
        "camera_make": metadata.get("EXIF:Make"),
        "camera_model": metadata.get("EXIF:Model"),
        "gps_latitude": metadata.get("EXIF:GPSLatitude"),
        "gps_longitude": metadata.get("EXIF:GPSLongitude"),
        "author": metadata.get("PDF:Author") or metadata.get("Author"),
        "creator": metadata.get("PDF:Creator") or metadata.get("Creator"),
    }

    # Flatten remaining raw metadata keys (avoid clobbering core keys)
    for k, v in metadata.items():
        sk = _sanitize_key(str(k))
        if sk not in normalized and v is not None:
            try:
                normalized[sk] = str(v)
            except Exception:
                normalized[sk] = repr(v)

    normalized["raw_metadata"] = metadata
    return {k: v for k, v in normalized.items() if v is not None}