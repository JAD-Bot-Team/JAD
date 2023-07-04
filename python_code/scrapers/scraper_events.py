import requests
from bs4 import BeautifulSoup

def scrape_events_from_url():
    url = 'https://www.calendar.jo'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    events = []
    event_boxes = soup.find_all('div', class_='ceventbox')
    for box in event_boxes:
        event = {}
        image_box = box.find('div', class_='imgbox')
        event['image_url'] = url + image_box.find('img')['src']
        title_box = box.find('h4')
        event['title'] = title_box.find('a').text.strip()
        event['link'] = url + title_box.find('a')['href']
        event['category'] = box.find('span', class_='greencolor').text.strip()
        event['location'] = box.find('p', class_='location').text.strip()
        event['dates'] = box.find('ul', class_='dates').text.strip()
        events.append(event)

    # Convert events to a list of strings separated by a newline
    event_strings = []
    for event in events:
        event_string = '\n'.join([
            f"Image URL: {event['image_url']}",
            f"Title: {event['title']}",
            f"Link: {event['link']}",
            f"Category: {event['category']}",
            f"Location: {event['location']}",
            f"Dates: {event['dates']}",
        ])
        event_strings.append(event_string)

    return event_strings

# print(scrape_events_from_url())