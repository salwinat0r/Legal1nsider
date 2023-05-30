# Legal1nsider

Simplifying proof-reading Legal documents using AI!

## Table of Contents
- [Background](#background)
- [Installation](#installation)
- [API](#api)
- [Usage](#usage)


<h2>Background</h2>
Proofreading legal documents manually is a challenging and time-consuming task due to their complexity. However, AI-powered tools have significantly eased this burden. They enhance efficiency and ensure adherence to legal writing standards. Combining AI with human expertise improves the accuracy of proofreading legal documents, saving time and effort in the process.

<h2>Installation</h2>
To install the necessary dependencies for this project, run the following command:

```python
pip install -r requirements.txt
```
Extract the clauses from a Word document and write them in two files

```python
from gen_engine import extract_clauses_from_document

extracted_clauses = extract_clauses_from_document(file_path)
clause_counter = Counter([clause["clause_name"] for clause in extracted_clauses])
most_common_clauses = clause_counter.most_common(5)
print(most_common_clauses)

```

Generate clause definition for a missing clause

```python
from gen_engine import extract_title, generate_response
from check import missing_clause

title = extract_title(file_path)
clause = missing_clause("clauses.txt", "test_clauses.txt")
prompt = f"Generate a {clause} clause for a {title} document"
suggested_clause = generate_response(prompt)
print(suggested_clause)

```


<h2>API</h2>

The POST methods in the `main.py` file:

```python
"/upload-document"
```
This will return the most common clauses and the missing clauses from the uploaded document

```json
{
  "most_common_clauses": [
    {
      "clause_name": "Drag Along Notice",
      "clause_number": "20.1(iv)"
    },
    {
      "clause_name": "Drag Along Purchaser",
      "clause_number": "20.1(ii)"
    },
    {
      "clause_name": "Drag Along Right",
      "clause_number": "20.1(ii)"
    },
    {
      "clause_name": "Drag Completion Date",
      "clause_number": "20.1(iv)"
    },
    {
      "clause_name": "Drag Shares",
      "clause_number": "20.1"
    }
  ],
  "missing_clause": "Drag Along Notice"
}
```

```python
"/generate_clause"
```
This route will return a suggested definition for the missing clause from the uploaded document

```json
{
  "response": "\"Drag Along Notice Clause:\n\nIf the company receives a bona fide offer to purchase all of the Company's shares from a third party, the majority shareholder(s) shall have the right to require the minority shareholder(s) to participate in the sale. Such request must be made in writing, stating the terms and conditions of the offer and providing the minority shareholder(s) with thirty (30) days' notice. \n\nUpon receipt of such notice, the minority shareholder(s) shall be obligated to sell their shares on the same terms and conditions as the majority shareholder(s), including any provisions relating to representations, warranties, covenants, and indemnification. \""
}
```

<h2> Usage </h2>

Firstly, copy your OPENAI API key to a txt file to run the ChatGPT API

```bash
touch key.txt
```

Now run,

```bash
uvicorn main:app --reload
```
and open this localhost URL on your browser `http://127.0.0.1:8000/docs`. This will open the Swagger UI kit for FastAPI backend.

- The files `clauses.txt` and `test_clauses.txt` clauses are extracted for the file  `SampleDocs\Testing\Draft SHA_Belita_11082015_Clean_Execution Version (1).docx`.

- Expand the `/upload-document` API route, click Try it Out and upload the above document.

- Now do the same for `/generate_clause` API route and upload the same document to generate a clause definition.