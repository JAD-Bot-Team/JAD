from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from time import sleep

def get_product_amazon(query):
    edited_text = query.split("-")
    query = edited_text[1]
    search_query = query.replace(" ", "")
    link_of_first_page_of_search_result = f"https://www.amazon.com/s?k={search_query}&ref=nb_sb_noss"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for page_number in range(1):
            link = link_of_first_page_of_search_result + f'&page={page_number}'

            page.goto(link, timeout=1000000)

            try:
                products_section = page.query_selector("//*[@id='search']/div[1]/div[1]/div")
            except:
                print('not found')
            else:
                sleep(1)
                html = products_section.inner_html()

            soup = BeautifulSoup(html, 'html.parser')
            all_cards = soup.find_all('div', class_='a-section a-spacing-base')
            best = 1000000
            num = 1
            amazon_products = []
            for card in all_cards:
                product = {}
                
                image_url = card.find('img', class_='s-image').get('src')
                product_link = card.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').get('href')
                products_title = card.find('span', class_='a-size-base-plus a-color-base a-text-normal')

                if products_title is not None:
                    products_title = products_title.get_text(strip=True)
                else:
                    products_title = "N/A"
            
                try:
                    total_reviews = card.find('div', class_='a-row a-size-small').find('span', class_='a-size-base s-underline-text').get_text(strip=True)
                except:
                    total_reviews = None
                
                try:
                    rating = card.find('div', class_='a-row a-size-small').find('span', class_='a-size-base').get_text(strip=True)
                except:
                    rating = None
                
                try:
                    price = card.find('span', class_='a-price').find('span', class_='a-offscreen').get_text(strip=True)
                except:
                    price = None
                
                product['Title'] = products_title
                product['link'] = f"https://www.amazon.com{product_link}"
                product['price'] = price
                int_price_1 = price.replace("$","").replace(",","")
                int_price = float(int_price_1)

                product['image_url'] = image_url
                if int_price <= best:
                    best = int_price

                amazon_products.append(product)

                num += 1
                if num == 6:
                    break
    best_price_str = f"Best price is: {best}$\n"

    # Format each product's information as a string separated by newlines
    product_strings = []
    for product in amazon_products:
        product_str = ""
        product_str += f"Title: {product['Title']} \n"
        product_str += f"Link: {product['link']} \n"
        product_str += f"Price: {product['price']} \n"
        product_strings.append(product_str)
    if best != 1000000:
        product_strings.append(best_price_str)
    if not product_strings:
        print("Sent Nothing")
        return ["No results were found, try something else"]

    print("Sent top 5 amazon products 🚀")
    return product_strings
