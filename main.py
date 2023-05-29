from fastapi import FastAPI, UploadFile, File
from docx import Document
import json
import re
from collections import Counter
from gen_engine import extract_clauses_from_document, extract_title

app = FastAPI(title = "Clause Extraction")

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = f"output_docs/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())


    # extract title
    title = extract_title(file_path)

    extracted_clauses = extract_clauses_from_document(file_path)
    # Extract clauses from the document
    clause_counter = Counter([clause["clause_name"] for clause in extracted_clauses])
    most_common_clauses = clause_counter.most_common(20)  # Get the top 5 most common clauses

    response = []
    for clause_name, count in most_common_clauses:
        clause_number = ""
        for clause in extracted_clauses:
            if clause["clause_name"] == clause_name:
                clause_number = clause["clause_number"]
                break
        response.append({"clause_name": clause_name, "clause_number": clause_number})
        with open('test_clauses.txt', 'w') as fp:
            json.dump(response, fp)

    return {"title": title, "most_common_clauses": response}

