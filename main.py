from fastapi import FastAPI, UploadFile, File
import numpy as np
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.post("/documents")
async def upload_document(document: UploadFile = File(...)):
    contents = await document.read()
    # Perform operations on the document
    return {"filename": document.filename}