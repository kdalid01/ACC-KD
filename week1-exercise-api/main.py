from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    # This endpoint runs when the browser opens http://127.0.0.1:8000/
    return {"message": "Hello from my exercise API"}

@app.get("/about")
def about():
    # This endpoint runs when the browser opens http://127.0.0.1:8000/about
    return {"name": "Week 1 Exercise API",
    "version": "1.0.0",
    "author": "Katusha"
    }