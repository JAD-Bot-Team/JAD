import requests
from bs4 import BeautifulSoup
from time import sleep

def get_product_dna(query):
    edited_text = query.split("-")
    query = edited_text[1]
    query = query.replace(" ", "*+")
    query_url = f"https://www.dna.jo/search?type=product&q={query}*"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(query_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    products_titles = soup.find_all('h2', class_='productitem--title')
    products = []

    for title in products_titles:
        product = {}
        product['title'] = title.text.strip()
        product['link'] = "https://www.dna.jo/" + title.a['href']
        price = title.find_next('div', class_="price--main")
        product['Price'] = price.text.strip()
        if not any(p['title'] == product['title'] for p in products):
            products.append(product)
        if len(products) == 5:
            break
    product_strings = [f"Title: {p['title']}\nLink: {p['link']}\nPrice: {p['Price']}\n" for p in products]
    return product_strings

if __name__ == "__main__":
    pass
    # dnas = get_product_dna("dna-laptop msi gaming")
    # for dna in dnas:
    #     print(dna)


