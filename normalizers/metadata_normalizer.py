def normalize_metadata(metadata):
    """
    Normalize metadata by keeping all exiftool fields
    but standardizing common field names
    """
    normalized = {
        # Generic file properties
        "filename": metadata.get("File:FileName"),
        "directory": metadata.get("File:Directory"),
        "file_size": metadata.get("File:FileSize"),
        "mime_type": metadata.get("File:MIMEType"),
        "created": metadata.get("File:FileCreateDate"),
        "modified": metadata.get("File:FileModifyDate"),
        
        # Image properties
        "camera_make": metadata.get("EXIF:Make"),
        "camera_model": metadata.get("EXIF:Model"),
        "gps_latitude": metadata.get("EXIF:GPSLatitude"),
        "gps_longitude": metadata.get("EXIF:GPSLongitude"),
        
        # Document properties
        "author": metadata.get("PDF:Author") or metadata.get("Author"),
        "creator": metadata.get("PDF:Creator") or metadata.get("Creator"),
        
        # Keep ALL raw metadata so nothing is lost
        "raw_metadata": metadata
    }
    
    # Remove None values to keep output clean
    return {k: v for k, v in normalized.items() if v is not None}