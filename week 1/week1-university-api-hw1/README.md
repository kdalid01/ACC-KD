# University API

My first simple REST API buit with FastAPI.

## Description

The API provides information about university students and returns:

- Viewing API information
- Viewing all students
- Viewing a single student by ID
- Returning a 404 error when a student does not exist

## Requirements

- Python
- FastAPI
- Uvicorn

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install requirements (required packages):

```powershell
pip install -r requirements.txt
```

## Run the API

Start the server:

```powershell
uvicorn main:app --reload
```

## Test URLs

### Home page

http://127.0.0.1:8000/

### Get All Student records

http://127.0.0.1:8000/students/

### Get Student s1 Returns John Smith

http://127.0.0.1:8000/students/s1

### Get Student s2 Returns Maria Garcia

http://127.0.0.1:8000/students/s2

### Test 404 Error Returns:

```json
{
  "detail": "Student not found"
}
```

URL:

http://127.0.0.1:8000/students/s10