import datetime
import requests
from bs4 import BeautifulSoup

def get_product_DNA():
  
    url='https://www.dna.jo/search?type=product&q=phone*'
    # Add a user-agent header to the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)

    # Find all the product titles within <div> tags and class "dynamic-module-title"
    products_titles = soup.find_all('h2', class_='productitem--title')
    products_link=soup.find_all()

    # Initialize a list to store product details
    products = []

    # Extract the details for each product
    for title in products_titles:
        product = {}

    #     # Get the product title
        product['title'] = title.text.strip()
        # print(title.text.strip())

        # Get the newegg link for the product
        product['link'] ="https://www.dna.jo/" + title.a['href']
        # print("https://www.dna.jo/" + title.a['href'])  
        
        # Get the product poster link (if available)
        poster = title.find_next("figure", class_="productitem--image")
        if poster and poster.img:
            product['poster_link'] = poster.img['src']
            # print(poster.img['src'])
        else:
            product['poster_link'] = None

        # Get the product rating (if available)
        price = title.find_next('div', class_="price--main")
        product['Price'] = price.text.strip()
        # print(price.text.strip())
       



        # Add the product details to the list
        products.append(product)

    # Print the products list
    print(products)

    # Return the top five products as separate strings
    # top_five_products = []
    # for product in products[:5]:
    #     product_str = ""
    #     product_str += f"Title: {product['title']}\n"
    #     # product_str += f"Link: {product['link']}\n"
    #     product_str += f"Poster Link: {product['poster_link']}\n"
    #     product_str += f"Rating: {product['rating']}\n"
    #     product_str += f"Description: {product['description']}\n"
    #     top_five_products.append(product_str)


if __name__ == "__main__":
    get_product_DNA()