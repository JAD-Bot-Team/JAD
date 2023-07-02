import requests
from bs4 import BeautifulSoup
import random

# def get_viki_anime():
url = "https://www.viki.com/categories/country/korea/genre/all"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

viki_title = soup.find_all("div", class_="sc-vebauh-0 ilalLZ")
print(viki_title)
# movies = []