import requests
from bs4 import BeautifulSoup

def get_trending_in_cinemas_jordan():
    url = "https://elcinema.com/en/now/jo/"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    listings = soup.find_all('div', attrs={'class': 'row'})

    movie_details = []
    unique_movies = set()

    for listing in listings:
        name = listing.find('h3', text=True)
        if name:
            movie_name = name.a.get_text()
            if movie_name not in unique_movies:
                movie = {'Name': movie_name}

                try:
                    link = listing.find('h3', text=True).a
                    if link:
                        movie['Link'] = f"https://elcinema.com{link.get('href')}"
                except AttributeError:
                    continue

                movie_details.append(movie)
                unique_movies.add(movie_name)

    return [f"Title: {movie['Name']}\nLink: {movie['Link']}\n\n" for movie in movie_details]


# movies = get_trending_in_cinemas_jordan()

# for movie in movies:
#     print(movie)







