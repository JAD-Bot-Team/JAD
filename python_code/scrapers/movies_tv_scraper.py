import os
import json
import datetime
import requests
from bs4 import BeautifulSoup
import sys

def top_action_movies():
    url = "https://www.imdb.com/search/title/?genres=Action&explore=genres&title_type=feature&ref_=ft_movie_0"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <h3> tags and class "lister-item-header"
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie poster link (if available)
        poster = title.find_next("div", class_="lister-item-image")
        if poster and poster.img:
            movie['poster_link'] = poster.img['src']
        else:
            movie['poster_link'] = None

        # Get the movie rating (if available)
        rating = title.find_next("div", class_="ratings-imdb-rating")
        if rating and rating.strong:
            movie['rating'] = rating.strong.text.strip()
        else:
            movie['rating'] = None

        # Get the movie description (if available)
        description = title.find_next("div", class_="lister-item-content")
        if description and description.find("p", class_="text-muted"):
            movie['description'] = description.find("p", class_="text-muted").text.strip()
        else:
            movie['description'] = None

        # Add the movie details to the list
        movies.append(movie)

    # Return the top five movies as separate strings
    top_five_movies = []
    for movie in movies[:5]:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Poster Link: {movie['poster_link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        movie_str += f"Description: {movie['description']}\n"
        top_five_movies.append(movie_str)
    print("Sent top 5 Action movies 🚀")
    return top_five_movies

def top_comedy_movies():
    url = "https://www.imdb.com/search/title/?genres=Comedy&explore=genres&title_type=feature&ref_=ft_movie_4"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <h3> tags and class "lister-item-header"
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie poster link (if available)
        poster = title.find_next("div", class_="lister-item-image")
        if poster and poster.img:
            movie['poster_link'] = poster.img['src']
        else:
            movie['poster_link'] = None

        # Get the movie rating (if available)
        rating = title.find_next("div", class_="ratings-imdb-rating")
        if rating and rating.strong:
            movie['rating'] = rating.strong.text.strip()
        else:
            movie['rating'] = None

        # Get the movie description (if available)
        description = title.find_next("div", class_="lister-item-content")
        if description and description.find("p", class_="text-muted"):
            movie['description'] = description.find("p", class_="text-muted").text.strip()
        else:
            movie['description'] = None

        # Add the movie details to the list
        movies.append(movie)

    # Return the top five movies as separate strings
    top_five_movies = []
    for movie in movies[:5]:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Poster Link: {movie['poster_link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        movie_str += f"Description: {movie['description']}\n"
        top_five_movies.append(movie_str)
    print("Sent top 5 Comdedy movies 🚀")
    return top_five_movies

def top_horror_movies():
    url = "https://www.imdb.com/search/title/?genres=Horror&explore=genres&title_type=feature&ref_=ft_movie_12"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <h3> tags and class "lister-item-header"
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie poster link (if available)
        poster = title.find_next("div", class_="lister-item-image")
        if poster and poster.img:
            movie['poster_link'] = poster.img['src']
        else:
            movie['poster_link'] = None

        # Get the movie rating (if available)
        rating = title.find_next("div", class_="ratings-imdb-rating")
        if rating and rating.strong:
            movie['rating'] = rating.strong.text.strip()
        else:
            movie['rating'] = None

        # Get the movie description (if available)
        description = title.find_next("div", class_="lister-item-content")
        if description and description.find("p", class_="text-muted"):
            movie['description'] = description.find("p", class_="text-muted").text.strip()
        else:
            movie['description'] = None

        # Add the movie details to the list
        movies.append(movie)

    # Return the top five movies as separate strings
    top_five_movies = []
    for movie in movies[:5]:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Poster Link: {movie['poster_link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        movie_str += f"Description: {movie['description']}\n"
        top_five_movies.append(movie_str)
    print("Sent top 5 Horror movies 🚀")
    return top_five_movies

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




############################################ TV Shows ############################################
############################################ TV Shows ############################################
############################################ TV Shows ############################################


def top_action_tv_shows():
    url = "https://www.imdb.com/search/title/?genres=Action&explore=genres&title_type=tv_series%2Cmini_series&ref_=ft_tv_0"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <h3> tags and class "lister-item-header"
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie poster link (if available)
        poster = title.find_next("div", class_="lister-item-image")
        if poster and poster.img:
            movie['poster_link'] = poster.img['src']
        else:
            movie['poster_link'] = None

        # Get the movie rating (if available)
        rating = title.find_next("div", class_="ratings-imdb-rating")
        if rating and rating.strong:
            movie['rating'] = rating.strong.text.strip()
        else:
            movie['rating'] = None

        # Get the movie description (if available)
        description = title.find_next("div", class_="lister-item-content")
        if description and description.find("p", class_="text-muted"):
            movie['description'] = description.find("p", class_="text-muted").text.strip()
        else:
            movie['description'] = None

        # Add the movie details to the list
        movies.append(movie)

    # Return the top five movies as separate strings
    top_five_movies = []
    for movie in movies[:5]:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Poster Link: {movie['poster_link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        movie_str += f"Description: {movie['description']}\n"
        top_five_movies.append(movie_str)
    print("Sent top 5 Action tv shows 🚀")
    return top_five_movies

def top_comedy_tv_shows():
    url = "https://www.imdb.com/search/title/?genres=Comedy&explore=genres&title_type=tv_series%2Cmini_series&ref_=ft_tv_4"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <h3> tags and class "lister-item-header"
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie poster link (if available)
        poster = title.find_next("div", class_="lister-item-image")
        if poster and poster.img:
            movie['poster_link'] = poster.img['src']
        else:
            movie['poster_link'] = None

        # Get the movie rating (if available)
        rating = title.find_next("div", class_="ratings-imdb-rating")
        if rating and rating.strong:
            movie['rating'] = rating.strong.text.strip()
        else:
            movie['rating'] = None

        # Get the movie description (if available)
        description = title.find_next("div", class_="lister-item-content")
        if description and description.find("p", class_="text-muted"):
            movie['description'] = description.find("p", class_="text-muted").text.strip()
        else:
            movie['description'] = None

        # Add the movie details to the list
        movies.append(movie)

    # Return the top five movies as separate strings
    top_five_movies = []
    for movie in movies[:5]:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Poster Link: {movie['poster_link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        movie_str += f"Description: {movie['description']}\n"
        top_five_movies.append(movie_str)
    print("Sent top 5 Comdedy tv shows 🚀")
    return top_five_movies

def top_horror_tv_shows():
    url = "https://www.imdb.com/search/title/?genres=Horror&explore=genres&title_type=tv_series%2Cmini_series&ref_=ft_tv_12"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the movie titles within <h3> tags and class "lister-item-header"
    movie_titles = soup.find_all("h3", class_="lister-item-header")

    # Initialize a list to store movie details
    movies = []

    # Extract the details for each movie
    for title in movie_titles:
        movie = {}

        # Get the movie title
        movie['title'] = title.a.text.strip()

        # Get the IMDb link for the movie
        movie['link'] = "https://www.imdb.com" + title.a['href']

        # Get the movie poster link (if available)
        poster = title.find_next("div", class_="lister-item-image")
        if poster and poster.img:
            movie['poster_link'] = poster.img['src']
        else:
            movie['poster_link'] = None

        # Get the movie rating (if available)
        rating = title.find_next("div", class_="ratings-imdb-rating")
        if rating and rating.strong:
            movie['rating'] = rating.strong.text.strip()
        else:
            movie['rating'] = None

        # Get the movie description (if available)
        description = title.find_next("div", class_="lister-item-content")
        if description and description.find("p", class_="text-muted"):
            movie['description'] = description.find("p", class_="text-muted").text.strip()
        else:
            movie['description'] = None

        # Add the movie details to the list
        movies.append(movie)

    # Return the top five movies as separate strings
    top_five_movies = []
    for movie in movies[:5]:
        movie_str = ""
        movie_str += f"Title: {movie['title']}\n"
        movie_str += f"IMDb Link: {movie['link']}\n"
        movie_str += f"Poster Link: {movie['poster_link']}\n"
        movie_str += f"Rating: {movie['rating']}\n"
        movie_str += f"Description: {movie['description']}\n"
        top_five_movies.append(movie_str)
    print("Sent top 5 Horror tv shows 🚀")
    return top_five_movies

# def top_10_rated_tv_shows():
#     url = "https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=75SEDC7QBKAPM1C8PWF8&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_6"

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
#     print("Sent top 10 rated tv shows 🚀")
#     return top_ten_movies

def top_10_rated_tv_shows():
    url = "https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=75SEDC7QBKAPM1C8PWF8&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_6"

    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the TV show titles within <td> tags and class "titleColumn"
    tv_show_titles = soup.find_all("td", class_="titleColumn")

    # Initialize a list to store TV show details
    tv_shows = []

    # Extract the details for each TV show
    for title in tv_show_titles[:10]:
        tv_show = {}

        # Get the TV show title
        tv_show['title'] = title.a.text.strip()

        # Get the IMDb link for the TV show
        tv_show['link'] = "https://www.imdb.com" + title.a['href']

        # Get the TV show rating
        rating = title.find_next("td", class_="ratingColumn imdbRating")
        tv_show['rating'] = rating.text.strip()

        # Add the TV show details to the list
        tv_shows.append(tv_show)

    # Return the top ten TV shows as separate strings
    top_ten_tv_shows = []
    for tv_show in tv_shows:
        tv_show_str = ""
        tv_show_str += f"Title: {tv_show['title']}\n"
        tv_show_str += f"IMDb Link: {tv_show['link']}\n"
        tv_show_str += f"Rating: {tv_show['rating']}\n"
        top_ten_tv_shows.append(tv_show_str)
    print("Sent top 10 rated TV shows 🚀")
    return top_ten_tv_shows



