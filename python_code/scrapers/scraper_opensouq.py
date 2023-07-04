import sys
import requests
from bs4 import BeautifulSoup

def get_product_open_souq(query):
    edited_text = query.split("-")
    query = edited_text[1]
    url = f"https://jo.opensooq.com/ar/find?term={query}"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    listings_ = soup.find('div', attrs={'id': "listing_posts"})
    listings = listings_.find_all('div', class_='mb-32 relative')

    products = []
    num = 0
    for listing in listings:
        links = listing.find_all('a', class_="flex flexNoWrap p-16 blackColor radius-8 grayHoverBg ripple boxShadow2 relative")
        for link in links:
            product = {}

            link_ = link.get('href')
            product_link = f"https://jo.opensooq.com{link_}"
            product['link'] = product_link

            prices = link.find_all('div', class_="sc-5f3d9e25-3 cyIeGw postDet flex-1 flex flexSpaceBetween flexDirectionColumn")
            for price in prices:
                num += 1
                price_elements = price.find_all('div', class_="postPrice ms-auto bold alignSelfCenter font-19")
                if price_elements:
                    product_price = price_elements[0].get_text()
                    product['price'] = product_price

            products.append(product)
        if num == 5:
            break

    product_strings = []
    for product in products:
        product_str = ""
        if 'price' in product:
            product_str += f"Price: {product['price']}"
            product_str += "\n"
            
        product_str += f"Link: {product['link']}"
        product_str += "\n"
        
        product_strings.append(product_str)

    # Reconfigure the stdout encoding to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')

    return product_strings

# print(get_product_open_souq("opensouq- كونا"))

