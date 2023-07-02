import requests
from bs4 import BeautifulSoup

def get_movie_details():
    url = "https://tajcinemas.com" 
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    listings = soup.find_all('div', attrs={'class':"row movie-tabs"})
    output = []
    for listing in listings:
        name = listing.find('h3').get_text()
        image_ = listing.find('img').get('src')
        image = f"https://tajcinemas.com{image_}"
        links_ = listing.find('a', class_='arrow-button').get('href')
        links = f"https://tajcinemas.com{links_}"
        output.append(name)
        output.append(image)
        output.append(links)
    return output
        
print(get_movie_details())
