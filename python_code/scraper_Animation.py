import requests
from bs4 import BeautifulSoup
import random

def get_10_Animation():
    url = "https://www.imdb.com/search/title/?genres=animation&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=94365f40-17a1-4450-9ea8-01159990ef7f&pf_rd_r=FDP1N20758RX3149N2KZ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_3"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    enime_title = soup.find_all("h3", class_="lister-item-header")

    movies = []

    for title in enime_title[:10]:
        movie = {}
        movie['title'] = title.text.strip()
        movie['link'] = "https://www.imdb.com/" + title.a['href']

        poster = title.find_next("div", class_="lister-item-image float-left")
        if poster and poster.img:
            movie['poster_link'] = poster.img['loadlate']
        else:
            movie['poster_link'] = None

        rating = title.find_next('div', class_="inline-block ratings-imdb-rating")
        if rating:
            movie['rating'] = rating.text.strip()
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
    get_10_Animation()
