import os
import json
import datetime
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from time import sleep


def get_product_newegg(query):
    edited_text = query.split("-")
    query = edited_text[1]
    print(query, 111111)
    url = f"https://www.newegg.com/p/pl?d={query}"
    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the product titles within <div> tags and class "dynamic-module-title"
    products_titles = soup.find_all("div", class_="dynamic-module-title")
    print(products_titles)
    # Initialize a list to store product details
    products = []

    # Extract the details for each product
    for title in products_titles:
        product = {}

        # Get the product title
        product['title'] = title.a.text.strip()

        # Get the newegg link for the product
        product['link'] = "https://www.newegg.com/" + title.a['href']

        # Get the product poster link (if available)
        poster = title.find_next("div", class_="dynamic-module-img")
        if poster and poster.img:
            product['poster_link'] = poster.img['src']
        else:
            product['poster_link'] = None

        # Get the product rating (if available)
        rating = title.find_next('span', class_="item-rating-num")
        if rating:
            product['rating'] = rating.text.strip()
        else:
            product['rating'] = None

        # Get the product description (if available)
        description = title.find_next("div", class_="item-action")
        if description and description.find("ul", class_="price"):
            product['description'] = description.find("ul", class_="price").text.strip()
        else:
            product['description'] = None

        # Add the product details to the list
        products.append(product)

    # Print the products list
    print(products)

    # Return the top five products as separate strings
    top_five_products = []
    for product in products[:5]:
        product_str = ""
        product_str += f"Title: {product['title']}\n"
        # product_str += f"Link: {product['link']}\n"
        product_str += f"Poster Link: {product['poster_link']}\n"
        product_str += f"Rating: {product['rating']}\n"
        product_str += f"Description: {product['description']}\n"
        top_five_products.append(product_str)
    print("Sent top 5 newegg products 🚀")
    return top_five_products




if __name__ == "__main__":
    get_product_newegg("product-headset")