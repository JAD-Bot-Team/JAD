import requests
from bs4 import BeautifulSoup
import random

def get_anime():
    url = "https://www.imdb.com/list/ls057577566/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    anime_title = soup.find_all("h3", class_="lister-item-header")

    anime_list = []

    for title in anime_title[:10]:
        anime = {}
        anime['title'] = title.text.strip()
        anime['link'] = "https://www.imdb.com/" + title.a['href']

        poster = title.find_next("div", class_="lister-item-image ribbonize")
        if poster and poster.img:
            anime['poster_link'] = poster.img['loadlate']
        else:
            anime['poster_link'] = None

        rating = title.find_next('div', class_="ipl-rating-star small")
        if rating:
            anime['rating'] = rating.text.strip()
        else:
            anime['rating'] = None     

        anime_list.append(anime)

    # Select three random anime from the list
    random_anime_list = random.sample(anime_list, 3)

    # Format the random anime data
    formatted_data = []
    for anime in random_anime_list:
        anime_data = []
        anime_data.append(f"Title: {anime['title']}")
        anime_data.append(f"Link: {anime['link']}")
        # anime_data.append(f"Poster Link: {anime['poster_link']}")
        anime_data.append(f"Rating: {anime['rating']}")
        formatted_data.append('\n'.join(anime_data))

    return formatted_data
