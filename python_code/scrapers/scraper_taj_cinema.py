# import requests
# from bs4 import BeautifulSoup
# import sys

# def get_movie_details():
#     url = "https://tajcinemas.com"
#     r = requests.get(url)
#     data = r.text
#     soup = BeautifulSoup(data, 'html.parser')
#     listings = soup.find_all('div', attrs={'class':"row movie-tabs"})
#     output = []
#     for listing in listings:
#         name = listing.find('h3').get_text()
#         image_ = listing.find('img').get('src')
#         image = f"https://tajcinemas.com{image_}"
#         links_ = listing.find('a', class_='arrow-button').get('href')
#         links = f"https://tajcinemas.com{links_}"
#         output.append(name)
#         output.append(image)
#         output.append(links)
#     return output

# movie_details = get_movie_details()

# # Set the encoding to UTF-8
# sys.stdout.reconfigure(encoding='utf-8')

# for detail in movie_details:
#     print(detail)



# import requests
# from bs4 import BeautifulSoup
# import sys

# def get_movie_details():
#     url = "https://tajcinemas.com"
#     r = requests.get(url)
#     data = r.text
#     soup = BeautifulSoup(data, 'html.parser')
#     listings = soup.find_all('div', attrs={'class': "row movie-tabs"})
#     output = []
#     for listing in listings:
#         name = listing.find('h3').get_text()
#         image_ = listing.find('img').get('src')
#         image = f"https://tajcinemas.com{image_}"
#         links_ = listing.find('a', class_='arrow-button').get('href')
#         links = f"https://tajcinemas.com{links_}"
#         movie_data = f"{name}\n{image}\n{links}"
#         output.append(movie_data)
#     sys.stdout.reconfigure(encoding='utf-8')
#     return '\n'.join(output)

# # Set the encoding to UTF-8

# movie_details = get_movie_details()
# print(movie_details)


# import requests
# from bs4 import BeautifulSoup

# def get_movie_details():
#     url = "https://tajcinemas.com"
#     r = requests.get(url)
#     data = r.text
#     soup = BeautifulSoup(data, 'html.parser')
#     listings = soup.find_all('div', attrs={'class': "row movie-tabs"})
#     output = []
#     sys.stdout.reconfigure(encoding='utf-8')
#     for listing in listings:
#         name = listing.find('h3').get_text()
#         image_ = listing.find('img').get('src')
#         image = f"https://tajcinemas.com{image_}"
#         links_ = listing.find('a', class_='arrow-button').get('href')
#         links = f"https://tajcinemas.com{links_}"
#         movie_data = f"{name}\n{image}\n{links}"
#         output.append(movie_data)
#     return output



# movies = get_movie_details()
# for movie in movies:
#     print(movie)
    
import sys
import requests
from bs4 import BeautifulSoup

def get_movie_details():
    url = "https://tajcinemas.com"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    listings = soup.find_all('div', attrs={'class': "row movie-tabs"})
    sys.stdout.reconfigure(encoding='utf-8')
    output = []
    seen_titles = []
    for listing in listings:
        name = listing.find('h3').get_text()
        image_ = listing.find('img').get('src')
        image = f"https://tajcinemas.com{image_}"
        links_ = listing.find('a', class_='arrow-button').get('href')
        links = f"https://tajcinemas.com{links_}"
        movie_data = f"{name}\n{image}\n{links}"
        if name not in seen_titles and 'taj' not in name.lower():
            output.append(movie_data)
            seen_titles.append(name)
    return output

# movies = get_movie_details()
# for movie in movies:
#     print(movie)


