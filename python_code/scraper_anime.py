import requests
from bs4 import BeautifulSoup
import random

def get_anime():
    url = "https://www.imdb.com/list/ls057577566/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    anime_title = soup.find_all("h3", class_="lister-item-header")
    # print(anime_title)
    movies = []

    for title in anime_title[:10]:
        movie = {}
        movie['title'] = title.text.strip()
        movie['link'] = "https://www.imdb.com/" + title.a['href']
        # print("https://www.imdb.com/" + title.a['href'])

        poster = title.find_next("div", class_="lister-item-image ribbonize")
        if poster and poster.img:
            movie['poster_link'] = poster.img['loadlate']
            # print(poster.img['loadlate'])
        else:
            movie['poster_link'] = None

        rating = title.find_next('div', class_="ipl-rating-star small")
        if rating:
            movie['rating'] = rating.text.strip()
            # print( rating.text.strip())
        else:
            movie['rating'] = None     

        movies.append(movie)   


    # Get a random movie from the list
    random_movie = random.choice(movies)
    print("Random Movie:")
    print("Title:", random_movie['title'])
    print("Link:", random_movie['link'])
    print("Poster Link:", random_movie['poster_link'])
    print("Rating:", random_movie['rating']) 


if __name__ == "__main__":
   get_anime()