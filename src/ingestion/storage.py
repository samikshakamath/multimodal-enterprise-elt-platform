from pathlib import Path
import shutil


def save_uploaded_file(file, document_type):
    """
    Save uploaded file into the appropriate landing zone.
    """

    storage_map = {
        "document": "data/documents",
        "image": "data/images",
        "transcript": "data/transcripts",
        "system_log": "data/logs",
        "unknown": "data/unknown"
    }

    destination_folder = Path(storage_map.get(document_type, "data/unknown"))

    destination_folder.mkdir(parents=True, exist_ok=True)

    file_path = destination_folder / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path)