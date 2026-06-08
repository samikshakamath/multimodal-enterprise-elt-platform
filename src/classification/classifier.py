from pathlib import Path


def classify_document(filename: str) -> str:
    """
    Determine document type based on file extension.
    """

    extension = Path(filename).suffix.lower()

    if extension == ".pdf":
        return "document"

    elif extension in [".jpg", ".jpeg", ".png"]:
        return "image"

    elif extension == ".txt":
        return "transcript"

    elif extension == ".log":
        return "system_log"

    else:
        return "unknown"