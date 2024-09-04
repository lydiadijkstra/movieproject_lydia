import statistics #library for calculating statistics
import random #library for finding a random movie
#import data #previous file with dictionary
import movie_storage #json file for storage


def leave_database():
    """
    nr. 0 - exit the database
    """
    return "Bye!"


def display_menu():
    """
    show the menu
    :return:
    """
    return """Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Filter movies"""


def display_movies():
    """
    Nr. 1 - displays the movies from the database
    :param movies: dictionary with movies-data
    """
    movies = movie_storage.get_movies()

    number_of_movies = len(movies)
    print(f'{number_of_movies} movies in total')
    for title, items in movies.items():
        print(f'{title} ({items["year"]}): {items["rating"]}')


def add_movie():
    """
    Nr. 2 - User add a movie incl rating and year
    :param movies:
    :return: new dictionary movies
    """
    movies = movie_storage.get_movies()

    while True:
        new_movie = input("Enter new movie: ").strip() #stripping whitespace
        if not new_movie:
            print("Movie name cannot be empty, please enter movie name!")
            continue
        if new_movie in movies:
            print("This movie is already listed!")
            continue
        break

    while True:
        new_movie_year = input("Enter new movie year: ").strip()
        if not new_movie_year:
            print("The year cannot be empty, please enter the year!")
            continue
        try:
            new_movie_year = int(new_movie_year)
            break
        except ValueError:
            print("Enter a valid year")

    while True:
        new_movie_rating = input("Enter new movie rating: ").strip()
        if not new_movie_rating:
            print("The rating cannot be empty, please enter the rating!")
            continue
        try:
            new_movie_rating = float(new_movie_rating)
            if new_movie_rating < 0 or new_movie_rating > 10:
                print("Rating can only be between 0 and 10, please enter correct rating!")
                continue
            break
        except ValueError:
            print("Enter a valid rating")
    movie_storage.add_new_movie(new_movie, new_movie_year, new_movie_rating)

    #movies[new_movie] = {"rating": new_movie_rating, "year": new_movie_year}
    print(f'Movie {new_movie} was successfully added')
    return movies


def delete_movie():
    """
    Nr.3 - Delete a movie from the dictionary
    :return: dict movies
    """
    movies = movie_storage.get_movies()

    while True:
        movie_to_delete = input("Enter movie name to delete: ")
        if movie_to_delete not in movies:
            print(f'Movie {movie_to_delete} does not exist')
            continue
        movie_storage.delete_movie(movie_to_delete)
        print(f'Movie {movie_to_delete} successfully deleted')
        break

    #del movies[movie_to_delete]
    return movies


def update_movie():
    """
    Nr. 4 - Update the rating and/or year of a movie
    :param movies: dict
    :return: updated dict
    """
    movies = movie_storage.get_movies()

    while True:
        movie_to_update = input("Enter movie name: ")
        if movie_to_update not in movies:
            print(f'Movie {movie_to_update} does not exist!')
            continue
        break
    while True:
        update_movie_rating = input("Enter new movie rating: ").strip()
        if not update_movie_rating:
            print("Rating cannot be empty, please enter valid rating!")
            continue
        try:
            update_movie_rating = float(update_movie_rating)
            if update_movie_rating < 0 or update_movie_rating > 10:
                print("Rating can only be between 0 and 10, please enter correct rating!")
                continue
            break
        except ValueError:
            print("Enter a valid rating")
    while True:
        update_movie_year = input("Enter new movie year: ").strip()
        if not update_movie_year:
            print("Year cannot be empty, please enter correct year!")
            continue
        try:
            update_movie_year = int(update_movie_year)
            break
        except ValueError:
            print("Enter a valid year")
    movie_storage.update_movie(movie_to_update, update_movie_rating, update_movie_year)

    #movies[movie_to_update] = {"rating": update_movie_rating}
    print(f'Movie {movie_to_update} successfully updated')
    return movies


def movie_stats():
    """
    Nr. 5 - Displays the statistiks
    :param movies: dict movies
    """
    movies = movie_storage.get_movies()

    print(average_rating(movies))
    print(median_rating(movies))
    print(best_rated_movie(movies))
    print(worst_rated_movie(movies))


def average_rating(movies):
    """
    calculates the average rating
    :param movies: dict movies
    :return: average rating of movies
    """
    total_rating = sum(movies[title]["rating"] for title in movies)
    avg_rating = round(total_rating / len(movies), 1)
    return f'Average rating: {avg_rating}'


def median_rating(movies):
    """
    calculates the median rating
    :param movies: dict movies
    :return: median rating of movies
    """
    ratings = [title["rating"] for title in movies.values()] #iterate over title-values in dict
    median_ratings = statistics.median(ratings)
    return f'Median rating: {median_ratings}'


def best_rated_movie(movies):
    """
    Analytics to find the best rated movie
    :param movies: dict movies
    :return: best rated movie
    """
    max_rating = 0
    for title, details in movies.items():
        if details["rating"] > max_rating:
            max_rating = details["rating"]
            best_movie_title = title
    return f'Best movie: {best_movie_title}, {max_rating})'


def worst_rated_movie(movies):
    """
    Analytics to find the worst rated movie
    :return: worst rated movie
    """
    min_rating = 10
    for title, details in movies.items():
        if details["rating"] < min_rating:
            min_rating = details["rating"]
            worst_movie_title = title
    return f'Worst movie: {worst_movie_title}, {min_rating}'


def random_movie():
    """
    Nr. 6 - Get a random suggestion for a movie with the random library
    :param movies: dictionary
    :return:random_choice_movie incl. rating
    """
    movies = movie_storage.get_movies()

    random_choice_movie = random.choice(list(movies.keys())) # creates a list of keys for random
    return f'Your movie for tonight: {random_choice_movie}, it is rated {movies[random_choice_movie]["rating"]}'


def search_for_title():
    """
    Nr. 7 - Search for a movie with a part of the title
    :param movies: dictionary
    """
    movies = movie_storage.get_movies()

    search_prompt = input("Enter part of moviename: ")
    search_outcome = {}
    for title, details in movies.items():
        if search_prompt in title.lower():
            search_outcome[title] = ["rating"]
            print(f'{title}, {details["rating"]}')


def movies_sorted_by_ratings():
    """
    Nr. 8 - Sorts the dict by ratings
    :param movies:
    :return:
    """
    movies = movie_storage.get_movies()

    movielist = list(movies.items())
    #Lambda = value[1] to the key x in the created tuple-list
    movielist.sort(key=lambda x: x[1]["rating"], reverse=True)
    for title, details in movielist:
        print(f'{title} ({details["year"]}): {details["rating"]}')


def movies_sorted_by_year():
    """
    Nr. 9 - Sorting by year, up or down
    :param movies: dict with movies
    :return: sorted products
    """
    movies = movie_storage.get_movies()

    movielist = list(movies.items())
    while True:
        decision_for_year_sorting = input("Do you want the latest movies first? (Y/N) ").lower()
        if decision_for_year_sorting == "y":
            movielist.sort(key=lambda x: x[1]["year"], reverse=True)
            for title, details in movielist:
                print(f'{title} ({details["year"]}): {details["rating"]}')
            break
        elif decision_for_year_sorting == "n":
            movielist.sort(key=lambda x: x[1]["year"])
            for title, details in movielist:
                print(f'{title} ({details["year"]}): {details["rating"]}')
            break
        else:
            print("Please enter 'Y' or 'N'")


def filter_movies():
    """
    Nr. 10 - Filters the movies with user-criteria
    :param movies: dict with movies
    :return:
    """
    movies = movie_storage.get_movies()

    while True:
        minimum_rating_user = input("Enter minimum rating (leave blank for no minimum rating): ")
        if minimum_rating_user == "":
            minimum_rating = None
            break
        try:
            minimum_rating = float(minimum_rating_user)
            break
        except ValueError:
            print("Invalid input. Please enter a valid rating.")
    while True:
        start_year_input = input("Enter start year (leave blank for no start year): ")
        if start_year_input == "":
            start_year = None
            break
        try:
            start_year = int(start_year_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    while True:
        end_year_input = input("Enter end year (leave blank for no end year):")
        if end_year_input == "":
            end_year = None
            break
        try:
            end_year = int(end_year_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    filtered_movies = []
    for title, details in movies.items():
        if (minimum_rating is None or minimum_rating <= details["rating"]) and \
        (start_year is None or start_year <= details["year"]) and \
        (end_year is None or end_year >= details["year"]):
            filtered_movies.append(f'{title} ({details["year"]}): {details["rating"]}')
    if filtered_movies:
        for movie in filtered_movies:
            print(movie)
    else:
        print("No result match these criteria")


def user_prompt():
    """
    prompt the user for his choice from menu
    :return: user input (prompt)
    """
    prompt = input("\nEnter choice (0-10): ")
    print("")
    if prompt == "0":
        print(leave_database())
        return False
    elif prompt == "1":
        display_movies()
    elif prompt == "2":
        add_movie()
    elif prompt == "3":
        delete_movie()
    elif prompt == "4":
        update_movie()
    elif prompt == "5":
        movie_stats()
    elif prompt == "6":
        print(random_movie())
    elif prompt == "7":
        search_for_title()
    elif prompt == "8":
        movies_sorted_by_ratings()
    elif prompt == "9":
        movies_sorted_by_year()
    elif prompt == "10":
        filter_movies()
    else:
        print("Invalid input, enter a valid number (0-10)")
    input("\nPress enter to continue ")
    return prompt


def main():
    """
    contains the while loop to loop until exit
    """
    """movies = data.get_movies()
    with open("movies_data.json", "w") as file:
        json.dump(movies, file)"""

    print("\n********** My Movies Database **********\n")
    while True:
        print(display_menu())
        prompt = user_prompt()
        if prompt is False:
            break

if __name__ == "__main__":
    main()
