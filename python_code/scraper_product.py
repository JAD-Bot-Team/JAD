import os
import json
import requests
from bs4 import BeautifulSoup
from time import sleep
import datetime

def get_product_newegg(query):
    edited_text = query.split("-")
    query = edited_text[1]
    print(query)
    url = f"https://www.newegg.com/p/pl?d={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    products_titles = soup.find_all("div", class_="dynamic-module-title")
    print(products_titles)
    products = []
    
    for title in products_titles:
        product = {}
        product['title'] = title.a.text.strip()
        product['link'] = "https://www.newegg.com/" + title.a['href']
        poster = title.find_next("div", class_="dynamic-module-img")
        if poster and poster.img:
            product['poster_link'] = poster.img['src']
        else:
            product['poster_link'] = None

        rating = title.find_next('span', class_="item-rating-num")
        if rating:
            product['rating'] = rating.text.strip()
        else:
            product['rating'] = None
        description = title.find_next("div", class_="item-action")
        if description and description.find("ul", class_="price"):
            product['description'] = description.find("ul", class_="price").text.strip()
        else:
            product['description'] = None
        products.append(product)
    print(products)

    top_five_products = []
    
    for product in products[:5]:
        product_str = ""
        product_str += f"Title: {product['title']}\n"
        product_str += f"Poster Link: {product['poster_link']}\n"
        product_str += f"Rating: {product['rating']}\n"
        product_str += f"Description: {product['description']}\n"
        top_five_products.append(product_str)
    print("Sent top 5 newegg products 🚀")
    return top_five_products

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


