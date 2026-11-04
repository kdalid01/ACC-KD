from fastapi import APIRouter, HTTPException

router = APIRouter()

students = {
    # The keys s1, s2, and s3 are the IDs used in the URL.
    "s1": {
        "name":"John Smith",
        "student_id":"S12345",
        "major":"Computer Science",
        "year":2
        },
    "s2": {
        "name":"Maria Garcia",
        "student_id":"S54321",
        "major":"Mathematics",
        "year":3
    },
    "s3": {
        "name":"Ali Khan",
        "student_id":"S77777",
        "major":"Data Science",
        "year":1
    }
}

@router.get("/")
def get_students():
    return students

@router.get("/{student_id}")
def get_student(student_id: str):
    student = students.get(student_id)
    
    # If ID is unknown, return a clear 404 error.
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
