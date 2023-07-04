import requests
from bs4 import BeautifulSoup

def get_5_books(query):
    edited_text = query.split("-")
    query = edited_text[1]
    url = f"https://www.goodreads.com/search?q={query}&qid=489fEJ7Tvc"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    book_titles = soup.find_all("a", class_="bookTitle")

    books = []

    for title in book_titles[:5]:
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

    # Format each book's information as a string separated by newlines
    book_strings = []
    for book in books:
        book_str = ""
        book_str += f"Title: {book['title']}\n"
        book_str += f"Link: {book['link']}\n"
        book_str += f"Poster Link: {book['poster_link']}\n"
        book_str += f"Rating: {book['rating']}\n"
        book_strings.append(book_str)

    return book_strings


# print(get_5_books())