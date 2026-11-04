# APIRouter lets this file define routes outside main.py. 
from fastapi import APIRouter, HTTPException

# This router will hold all movie-related end-points.
router = APIRouter()

# This dictionary is temporary in-memory data.
# Next week we will replace this style with SQL database data.
movies = {
    "hobbit": {
        "title": "The Hobbit",
        "description": "A fantasy adventure film based on the novel by J.R.R. Tolkien.",
        "year": 2012
    },
    "inception": {
        "title": "Inception",
        "description": "A mind-bending thriller about dreams within dreams.",
        "year": 2010
    },
    "interstellar": {
        "title": "Interstellar",
        "description": "A science fiction epic exploring space and time.",
        "year": 2014
    },
    "matrix": {
        "title": "The Matrix",
        "description": "A science-fictionn film about a simulated reality",
        "year": 1999
    }
}


# This route will become /movies/ after we connect it in main.py.
@router.get("/")
def get_movies():
    #return all movie records.
    return movies

@router.get("/{movie_id}")
def get_movie(movie_id: str):
    # movie_id comes from the URL, for example /movies/hobbit/
    # We use it as a key in the movies dictionary.
    # .get() returns None instead of crashing if the key does not exist.
    movie = movies.get(movie_id)

    if movie is None:
    # If the movie_id is not found in the movies dictionary, we raise an HTTPException with a 404 status code and a detail message indicating that the movie was not found. This will result in a proper error response being sent back to the client.  
        raise HTTPException(status_code=404, detail="Movie not found")

        return movie