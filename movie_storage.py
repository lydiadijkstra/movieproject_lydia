import json

JSON_FILE = "movies_data.json"


def get_movies():
    """
    Retreives the data from the JSON file so it can be used in the programm
    :return: data from JSON File
    """
    data = ""
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def add_new_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    movies[title] = {
        "rating": rating,
        "year": year
    }

    with open(JSON_FILE, "w") as file:
        json.dump(movies, file)


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    movies = get_movies()

    with open(JSON_FILE, "w") as file:
        json.dump(movies, file)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    del movies[title]

    with open(JSON_FILE, "w") as file:
        json.dump(movies, file)


def update_movie(title, rating, year):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    movies[title] = {"year": year, "rating": rating}

    with open(JSON_FILE, "w") as file:
        json.dump(movies, file)