# Notes API

A simple CRUD API built with FastAPI and SQLite. The API allows users to create, read, update, and delete notes stored in a SQLite database.

# Project Setup

### 1. Create and open the project folder in VS Code

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

The terminal prompt should begin with:

```text
(.venv)
```

### 4. Create requirements.txt

```text
fastapi==0.141.1
uvicorn==0.52.4
```

### 5. Install the required packages

```powershell
python -m pip install -r requirements.txt
```

### 6. Create main.py

Add the FastAPI Notes CRUD app code from the lab instructions.

---

# Running the API

Start the server:

```powershell
python -m uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

Open the notes endpoint:

```text
http://127.0.0.1:8000/notes
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | / | Returns a welcome message |
| GET | /notes | Returns all notes |
| GET | /notes/{note_id} | Returns one note |
| POST | /notes | Creates a note |
| PATCH | /notes/{note_id} | Updates a note |
| DELETE | /notes/{note_id} | Deletes a note |

---

# Testing the API

## Testing the API using FastAPI documentation at:

```text
http://127.0.0.1:8000/docs
```

### 1. Create a Note

In `/docs`, expand **POST /notes**, click **Try it out**, and submit:

```json
{
  "title": "First note",
  "text": "This note is stored in SQLite."
}
```

Expected result:

- Status code: **201 Created**
- A new note is returned with an automatically generated ID

The returned ID was used for all subsequent tests.

### 2. Read All Notes

Open:

```text
http://127.0.0.1:8000/notes
```

Expected result:

- Status code: **200 OK**
- The list of notes includes the note created in the previous step

### 3. Read a Single Note

In `/docs`, expand **GET /notes/{note_id}**, enter the ID returned by POST, and click **Execute**.

Expected result:

- Status code: **200 OK**
- The created note is returned

### 4. Update a Note

In `/docs`, expand **PATCH /notes/{note_id}** and submit:

```json
{
  "title": "Updated first note"
}
```

Expected result:

- Status code: **200 OK**
- The title is updated
- The original text remains unchanged

The server was restarted and the note was requested again to confirm that the updated data was still stored in SQLite.

### 5. Delete a Note

In `/docs`, expand **DELETE /notes/{note_id}** and execute the request using the same ID.

Expected result:

- Status code: **200 OK**

Response:

```json
{
  "message": "Note deleted"
}
```

### 6. Test a Missing Note

After deleting the note, **GET /notes/{note_id}** was executed again using the same ID.

Expected result:

- Status code: **404 Not Found**

Response:

```json
{
  "detail": "Note not found"
}
```

### 7. Additional Validation Tests

The following error cases were tested:

**PATCH /notes/9999**

```json
{
  "title": "Missing note test"
}
```

Result:

- Status code: **404 Not Found**

**DELETE /notes/9999**

Result:

- Status code: **404 Not Found**

**POST /notes** with a missing required field:

```json
{
  "title": "Incomplete note"
}
```

Result:

- Status code: **422 Unprocessable Entity**

This confirms that FastAPI validation correctly rejects requests that do not match the required data model.

## Observed Status Codes

| Endpoint | Status |
|-----------|---------|
| POST /notes | 201 Created |
| GET /notes | 200 OK |
| GET /notes/{note_id} | 200 OK |
| PATCH /notes/{note_id} | 200 OK |
| DELETE /notes/{note_id} | 200 OK |
| GET missing note | 404 Not Found |
| PATCH missing note | 404 Not Found |
| DELETE missing note | 404 Not Found |
| Invalid POST request | 422 Unprocessable Entity |


## Testing the API using Postman Testing

The API was also tested using Postman to verify that all CRUD endpoints function correctly outside the FastAPI documentation interface.

The server remained running while all Postman requests were performed.

### 1. GET /notes

A GET request was sent to:

```text
http://127.0.0.1:8000/notes
```

Expected result:

- Status code: **200 OK**
- A JSON list of notes is returned

If no notes exist, the response is:

```json
[]
```

### 2. POST /notes

A POST request was sent to:

```text
http://127.0.0.1:8000/notes
```

Request body:

```json
{
  "title": "Postman note",
  "text": "I created this note using Postman."
}
```

Expected result:

- Status code: **201 Created**
- The response contains the new note ID, title, and text

Example response:

```json
{
  "id": 1,
  "title": "Postman note",
  "text": "I created this note using Postman."
}
```

The returned ID was recorded and used in subsequent tests.

### 3. PATCH /notes/{note_id}

A PATCH request was sent using the ID returned by the POST request.

Endpoint:

```text
http://127.0.0.1:8000/notes/{note_id}
```

Request body:

```json
{
  "title": "Updated from Postman"
}
```

Expected result:

- Status code: **200 OK**
- The title is updated
- The existing text remains unchanged

Example response:

```json
{
  "id": 1,
  "title": "Updated from Postman",
  "text": "I created this note using Postman."
}
```

### 4. DELETE /notes/{note_id}

A DELETE request was sent using the same ID.

Endpoint:

```text
http://127.0.0.1:8000/notes/{note_id}
```

Expected result:

- Status code: **200 OK**

Response:

```json
{
  "message": "Note deleted"
}
```

The note was successfully removed from the database.

### 5. Verify Deletion

After deletion, a GET request was sent for the same ID.

Endpoint:

```text
GET /notes/{note_id}
```

Expected result:

- Status code: **404 Not Found**

Response:

```json
{
  "detail": "Note not found"
}
```

This confirmed that the note had been permanently removed.

### 6. Additional Error Tests

#### 6.1 Missing Note

PATCH request:

```text
PATCH /notes/9999
```

Request body:

```json
{
  "title": "Missing note test"
}
```

Result:

```text
404 Not Found
```

DELETE request:

```text
DELETE /notes/9999
```

Result:

```text
404 Not Found
```

#### 6.2 Validation Error

POST request:

```json
{
  "title": "Incomplete note"
}
```

Result:

```text
422 Unprocessable Entity
```

The request failed because the required `text` field was missing from the request body.

### Conclusion

All CRUD operations were successfully tested using both FastAPI Docs and Postman. The API correctly created, read, updated, and deleted notes, while also returning appropriate error responses for missing resources and invalid request data.