import requests
from bs4 import BeautifulSoup


def get_books():
    query = "enemy"
    url = f"https://www.goodreads.com/search?q={query}&qid=489fEJ7Tvc"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    book_titles = soup.find_all("a", class_="bookTitle")

    books = []

    for title in book_titles:
        book = {}
        book['title'] = title.text.strip()
        book['link'] = "https://www.goodreads.com" + title['href']

        poster = title.find_next("a", class_="")
        if poster and poster.img:
            book['poster_link'] = poster.img['src']
        else:
            book['poster_link'] = None

        rating = title.find_next('span', class_="minirating")
        if rating:
            book['rating'] = rating.text.strip()
        else:
            book['rating'] = None

        books.append(book)

    return books


if __name__ == "__main__":
    books = get_books()
    for book in books:
        print("Title:", book['title'])
        print("Link:", book['link'])
        print("Poster Link:", book['poster_link'])
        print("Rating:", book['rating'])
        print()
