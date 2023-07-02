import requests
from bs4 import BeautifulSoup

query = "lay"
url = f"https://manybooks.net/search-book?search={query}&ga_submit=bsf%3Axfl7vYxXQafJXsY"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

novel_titles = soup.find_all("div", class_="field field--name-field-title field--type-string field--label-hidden field--item")

# Create a set to store unique titles
printed_titles = set()

for title in novel_titles:
    novel_title = title.text.strip()
    # Check if the title has already been printed
    if novel_title not in printed_titles:
        print("Novel Title:", novel_title)
        # Add the title to the set to avoid duplication
        printed_titles.add(novel_title)
