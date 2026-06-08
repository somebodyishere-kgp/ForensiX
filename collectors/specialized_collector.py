from analysers.metadata_extractor import (
    get_exiftool_metadata
)

from normalizers.metadata_normalizer import (
    normalize_metadata
)

from utils.hashing import (
    get_file_hashes
)

from routers.file_type_router import (
    get_file_type
)

from collectors.pdf_collector import (
    get_pdf_metadata
)

from collectors.office_collector import (
    get_docx_metadata
)

from collectors.audio_collector import (
    get_audio_metadata
)


def collect_specialized_metadata(file_path):
    """
    Route to specialized collectors based on file type
    Returns empty dict if no specialized handler exists
    """
    file_type = get_file_type(file_path)
    
    if file_type == "pdf":
        return get_pdf_metadata(file_path)
    
    if file_type == "docx":
        return get_docx_metadata(file_path)
    
    if file_type == "audio":
        return get_audio_metadata(file_path)
    
    return {}

def collect_metadata(file_path):
    """
    Main collection function: 
    - Get general metadata via ExifTool
    - Get specialized metadata via file-type-specific collectors
    - Merge everything together
    - Add hashes
    """
    try:
        # Step 1: Get general metadata via exiftool (everything)
        general_metadata = get_exiftool_metadata(file_path)
        
        # Step 2: Get specialized metadata based on file type
        specialized_metadata = collect_specialized_metadata(file_path)
        
        # Step 3: Merge both (specialized overrides general)
        all_metadata = general_metadata.copy()
        all_metadata.update(specialized_metadata)
        
        # Step 4: Normalize field names
        normalized = normalize_metadata(all_metadata)
        
        # Step 5: Add hashes
        hashes = get_file_hashes(file_path)
        normalized.update(hashes)
        
        return normalized
        
    except Exception as e:
        return {
            "filename": str(file_path),
            "error": str(e)
        }