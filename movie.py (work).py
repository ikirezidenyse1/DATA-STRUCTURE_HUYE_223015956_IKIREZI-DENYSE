from collections import deque

# List of movies with MovieID, MovieName, and Genre
movies = [
    {"MovieID": 1, "MovieName": "Mad Max: Fury Road", "Genre": "Action"},
    {"MovieID": 2, "MovieName": "John Wick", "Genre": "Action"},
    {"MovieID": 3, "MovieName": "Die Hard", "Genre": "Action"},
    {"MovieID": 4, "MovieName": "The Hangover", "Genre": "Comedy"},
    {"MovieID": 5, "MovieName": "Superbad", "Genre": "Comedy"},
    {"MovieID": 6, "MovieName": "Anchorman", "Genre": "Comedy"},
    {"MovieID": 7, "MovieName": "The Godfather", "Genre": "Drama"},
    {"MovieID": 8, "MovieName": "Forrest Gump", "Genre": "Drama"},
    {"MovieID": 9, "MovieName": "Fight Club", "Genre": "Drama"},
    {"MovieID": 10, "MovieName": "The Exorcist", "Genre": "Horror"},
    {"MovieID": 11, "MovieName": "A Nightmare on Elm Street", "Genre": "Horror"},
    {"MovieID": 12, "MovieName": "The Conjuring", "Genre": "Horror"},
    {"MovieID": 13, "MovieName": "Interstellar", "Genre": "Sci-Fi"},
    {"MovieID": 14, "MovieName": "The Matrix", "Genre": "Sci-Fi"},
    {"MovieID": 15, "MovieName": "Inception", "Genre": "Sci-Fi"},
    {"MovieID": 16, "MovieName": "Pride and Prejudice", "Genre": "Romance"},
    {"MovieID": 17, "MovieName": "The Notebook", "Genre": "Romance"},
    {"MovieID": 18, "MovieName": "Titanic", "Genre": "Romance"},
    {"MovieID": 19, "MovieName": "Se7en", "Genre": "Thriller"},
    {"MovieID": 20, "MovieName": "Gone Girl", "Genre": "Thriller"},
    {"MovieID": 21, "MovieName": "Shutter Island", "Genre": "Thriller"},
    {"MovieID": 22, "MovieName": "Planet Earth", "Genre": "Documentary"},
    {"MovieID": 23, "MovieName": "13th", "Genre": "Documentary"},
    {"MovieID": 24, "MovieName": "Inside Job", "Genre": "Documentary"},
    {"MovieID": 25, "MovieName": "The Lord of the Rings", "Genre": "Fantasy"},
    {"MovieID": 26, "MovieName": "Harry Potter", "Genre": "Fantasy"},
    {"MovieID": 27, "MovieName": "The Hobbit", "Genre": "Fantasy"},
    {"MovieID": 28, "MovieName": "Indiana Jones", "Genre": "Adventure"},
    {"MovieID": 29, "MovieName": "Jumanji", "Genre": "Adventure"},
    {"MovieID": 30, "MovieName": "Pirates of the Caribbean", "Genre": "Adventure"},
]

# Stack for recently watched movies
recently_watched = []

# Queue for watchlist
watchlist = deque()

# Function to display available genres
def display_genres():
    print("\nAvailable Genres:")
    unique_genres = set(movie['Genre'] for movie in movies)
    for genre in unique_genres:
        print(f"- {genre}")

# Function to display movies within a selected genre
def display_movies_by_genre(genre):
    print(f"\nMovies in {genre} genre:")
    found_movies = [movie for movie in movies if movie['Genre'] == genre]
    if found_movies:
        for movie in found_movies:
            print(f"- {movie['MovieName']}")
    else:
        print(f"No movies found in the genre: {genre}")

# Function to add a movie to the watchlist/ buffer queue
def add_to_watchlist(movie_id):
    for movie in movies:
        if movie["MovieID"] == movie_id:
            watchlist.append(movie["MovieName"])
            print(f"Movie '{movie['MovieName']}' is added to the watchlist.")
            return
    print("Invalid Movie ID. Please choose a valid movie from the list.")

# Function to start watching the next movie in the watchlist/ buffer queue
def watch_next_movie():
    if watchlist:
        movie = watchlist.popleft()
        recently_watched.append(movie)
        print(f"You are now watching '{movie}'.")
    else:
        print("No movies in the watchlist to watch.")

# Function to view recently watched movies
def view_recently_watched():
    if recently_watched:
        print("\nRecently Watched Movies:")
        for movie in recently_watched[::-1]:  # Display the most recent movie at the top
            print(f"- {movie}")
    else:
        print("You haven't watched any movies yet.")

# Function to undo the last watched movie (remove from recently watched and return to buffer queue/watch list)
def undo_last_watched():
    if recently_watched:
        last_movie = recently_watched.pop()
        for movie in movies:
            if movie["MovieName"] == last_movie:
                watchlist.appendleft(last_movie)
                print(f"Undo successful: '{last_movie}' has been returned to the watchlist.")
                return
    else:
        print("No recently watched movies to undo.")

# Function to view movies in the buffer queue/watch list
def view_watchlist():
    if watchlist:
        print("\nMovies in Watchlist:")
        for movie in watchlist:
            print(f"- {movie}")
    else:
        print("No movies in the watchlist.")

# Main menu for interaction
def movie_streaming_platform():
    while True:
        print("\nOptions:")
        print("1. Display Available Genres")
        print("2. Display Movies by Genre")
        print("3. Add Movie to Watchlist")
        print("4. Watch Next Movie in Watchlist")
        print("5. View Recently Watched Movies")
        print("6. Undo Last Watched Movie")
        print("7. View Watchlist")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == '1':
            display_genres()
        elif choice == '2':
            display_genres()
            genre = input("Enter the genre to display movies: ")
            display_movies_by_genre(genre)
        elif choice == '3':
            try:
                movie_id = int(input("Enter the Movie ID to add to the watchlist: "))
                add_to_watchlist(movie_id)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            watch_next_movie()
        elif choice == '5':
            view_recently_watched()
        elif choice == '6':
            undo_last_watched()
        elif choice == '7':
            view_watchlist()
        elif choice == '8':
            print("Exiting movie streaming platform.")
            break
        else:
            print("Invalid choice, please select a valid option.")

# Run the movie streaming platform system
movie_streaming_platform()
