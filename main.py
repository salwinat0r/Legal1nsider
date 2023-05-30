from fastapi import FastAPI, UploadFile, File
from docx import Document
import json
import re
import os
from collections import Counter
from gen_engine import extract_clauses_from_document, extract_title, generate_response
from check import missing_clause

app = FastAPI(title = "Clause Extraction")

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = f"output_docs/{file.filename}"
    output_dir = os.path.dirname(file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(file_path, "wb") as f:
        f.write(await file.read())


    extracted_clauses = extract_clauses_from_document(file_path)
    # Extract clauses from the document
    clause_counter = Counter([clause["clause_name"] for clause in extracted_clauses])
    most_common_clauses = clause_counter.most_common(5)  # Get the top 5 most common clauses

    response = []
    for clause_name, count in most_common_clauses:
        clause_number = ""
        for clause in extracted_clauses:
            if clause["clause_name"] == clause_name:
                clause_number = clause["clause_number"]
                break
        response.append({"clause_name": clause_name, "clause_number": clause_number})
        # with open('test_clauses.txt', 'w') as fp:
        #     json.dump(response, fp)
    clause = missing_clause("clauses.txt", "test_clauses.txt")

    return {"most_common_clauses": response, "missing_clause": clause }


@app.post("/generate_clause")
async def generate_clause(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = f"output_docs/{file.filename}"
    output_dir = os.path.dirname(file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(file_path, "wb") as f:
        f.write(await file.read())
        
    title = extract_title(file_path)
    clause = missing_clause("clauses.txt", "test_clauses.txt")
    prompt = f"Generate a {clause} clause for a {title} document"
    suggested_clause = generate_response(prompt)
    return {"response": suggested_clause}