from fastapi import FastAPI
# Import the students router from routers/students.py.
from routers import students

app = FastAPI()

# Every route in students.py will start with /students.
app.include_router(students.router, prefix="/students")


@app.get("/")
def home():
    return {
        "name": "University API",
        "version": "1.0.0",
        "description": "A simple API to fetch university student data.",
        "endpoints": {
            "root": "GET /",
            "all_students": "GET /students",
            "student_by_id": "GET /students/s1"
        }
    }