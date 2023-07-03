import requests
from bs4 import BeautifulSoup


def get_movie_details(query):
    url = f"https://jo.opensooq.com/ar/find?term={query}" 
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    listings_ = soup.find('div', attrs={'id':"listing_posts"})
    listings = listings_.find_all('div', class_ = 'mb-32 relative')
    output = []
    num = 0
    for listing in listings:
        links = listing.find_all('a', class_ ="flex flexNoWrap p-16 blackColor radius-8 grayHoverBg ripple boxShadow2 relative")
        for i in links :
            link_ = i.get('href')
            link = f"https://jo.opensooq.com{link_}"
            output.append(link)
            price_=  i.find_all('div' , class_="sc-5f3d9e25-3 cyIeGw postDet flex-1 flex flexSpaceBetween flexDirectionColumn")
            for k in price_ :
                num += 1
                
                price = k.find_all('div', class_="postPrice ms-auto bold alignSelfCenter font-19")
                if price == [] :
                    pass
                
                else :
                    priiice = price[0].get_text()
                    output.append(priiice)

        if num == 5 :
            break
                    
                    
    # for i in output :
    #     print(i)
    return output
print(get_movie_details("kona"))
