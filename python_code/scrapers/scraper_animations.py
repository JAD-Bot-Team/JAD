import requests
from bs4 import BeautifulSoup
import random

def get_3_Animations():
    url = "https://www.imdb.com/search/title/?genres=animation&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=94365f40-17a1-4450-9ea8-01159990ef7f&pf_rd_r=FDP1N20758RX3149N2KZ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_3"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    animation_title = soup.find_all("h3", class_="lister-item-header")

    animation_list = []

    for title in random.sample(animation_title, 3):
        animation = {}
        animation['title'] = title.text.strip()
        animation['link'] = "https://www.imdb.com/" + title.a['href']

        poster = title.find_next("div", class_="lister-item-image float-left")
        if poster and poster.img:
            animation['poster_link'] = poster.img['loadlate']
        else:
            animation['poster_link'] = None

        rating = title.find_next('div', class_="inline-block ratings-imdb-rating")
        if rating:
            animation['rating'] = rating.text.strip()
        else:
            animation['rating'] = None     

        animation_list.append(animation)

    # Get formatted animation data as list of strings
    formatted_data = []
    for animation in animation_list:
        formatted_animation = []
        formatted_animation.append(f"Title: {animation['title']}")
        formatted_animation.append(f"Link: {animation['link']}")
        formatted_animation.append(f"Poster Link: {animation['poster_link']}")
        formatted_animation.append(f"Rating: {animation['rating']}")
        formatted_data.append('\n'.join(formatted_animation))

    return formatted_data


random_animation_data = get_3_Animations()
# print("Random Animation Data:")
# for animation in random_animation_data:
#     print(animation)
