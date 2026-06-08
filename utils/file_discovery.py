from pathlib import Path

def discover_files(target_path):
    """
    Recursively find all files inside a directory
    Returns a list of path objects
    """
    target = Path(target_path)

    if not target.exists():
        raise FileNotFoundError(
            f"Path does not exist: {target_path}"
        )
    
    files = [item for item in target.rglob("*") if item.is_file()]

    return files