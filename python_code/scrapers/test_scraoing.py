
# import requests
# from bs4 import BeautifulSoup

# def top_10_rated_movies():
#     url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

#     # Add a user-agent header to the request
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     response = requests.get(url, headers=headers)

#     # Create a BeautifulSoup object to parse the HTML content
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Find all the movie titles within <td> tags and class "titleColumn"
#     movie_titles = soup.find_all("td", class_="titleColumn")

#     # Initialize a list to store movie details
#     movies = []

#     # Extract the details for each movie
#     for title in movie_titles[:10]:
#         movie = {}

#         # Get the movie title
#         movie['title'] = title.a.text.strip()

#         # Get the IMDb link for the movie
#         movie['link'] = "https://www.imdb.com" + title.a['href']

#         # Get the movie rating
#         rating = title.find_next("td", class_="ratingColumn imdbRating")
#         movie['rating'] = rating.text.strip()

#         # Add the movie details to the list
#         movies.append(movie)

#     # Return the top ten movies as separate strings
#     top_ten_movies = []
#     for movie in movies:
#         movie_str = ""
#         movie_str += f"Title: {movie['title']}\n"
#         movie_str += f"IMDb Link: {movie['link']}\n"
#         movie_str += f"Rating: {movie['rating']}\n"
#         top_ten_movies.append(movie_str)
#     print("Sent top 10 rated movies 🚀")
#     return top_ten_movies


# movies = top_10_rated_movies()

# for movie in movies:
#     print(movie)

import requests
from bs4 import BeautifulSoup
import sys

def top_10_rated_movies():
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <td> tags and class "titleColumn"
    movie_titles = soup.find_all("td", class_="titleColumn")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles[:10]:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie rating
        rating = title.find_next("td", class_="ratingColumn imdbRating")
        movie['rating'] = rating.text.strip()

        # Add the movie details to the list
        movies.append(movie)

    # Return the top ten movies as separate strings
    top_ten_movies = []
    for movie in movies:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        top_ten_movies.append(movie_str)
    
    # Print the message using sys.stdout to handle Unicode characters
    message = "Sent top 10 rated movies 🚀"
    sys.stdout.buffer.write(message.encode('utf-8'))
    sys.stdout.buffer.write(b'\n')
    
    return top_ten_movies


# movies = top_10_rated_movies()

# for movie in movies:
#     print(movie)