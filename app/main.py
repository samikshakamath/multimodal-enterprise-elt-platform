from fastapi import FastAPI, UploadFile, File

from src.classification.classifier import classify_document
from src.ingestion.storage import save_uploaded_file


app = FastAPI(
    title="Multimodal Enterprise ELT Platform"
)


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    document_type = classify_document(file.filename)

    storage_location = save_uploaded_file(
        file=file,
        document_type=document_type
    )

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "document_type": document_type,
        "storage_location": storage_location,
        "processing_pipeline": f"{document_type}_pipeline"
    }