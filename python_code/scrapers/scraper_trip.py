import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_trips():
    results = []
    def scrape_trip(url):
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        section = soup.find('section', class_='ourdest')
        
        for div in section.find_all('div', class_='col-xs-12'):
            item = []
            a_tag = div.find('a')
            if a_tag:
                item.append(f"Link: {urljoin(url, a_tag['href'])}")
            h3 = div.find('h3')
            if h3:
                item.append(f"Title: {h3.text.strip()}")
            img = div.find('img')
            if img:
                if "https://www.jannah.jo" not in img:
                    item.append(f"Image Source: https://www.jannah.jo{img['src']}")
                item.append(f"Image Source: {img['src']}")
            span = div.find('span', class_='cbttn2')
            if span:
                item.append(f"Price: {span.text.strip()}")
            
            if item:  # Exclude items with no relevant information
                results.append('\n'.join(item))

    websites = [
        'https://www.jannah.jo/cities/amman',
        'https://www.jannah.jo/cities/irbid',
        'https://www.jannah.jo/cities/golden-triangle'
    ]

    for website in websites:
        scrape_trip(website)
    
    return results
