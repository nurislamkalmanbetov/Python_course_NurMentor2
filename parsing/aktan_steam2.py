import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    full_link = 'https://us.shop.battle.net/en-us'
    soup = BS(html, 'html.parser')
    container = soup.find('storefront-browsing-card-group-layout')
    test = container.find_all('li', class_='ng-star-inserted')    
    print(test)
    # if container:
    #     links = container.find_all('a', href=True)
    #     for link in links:
    #         print(full_link + link['href'])

if __name__ == "__main__":
    url = 'https://us.shop.battle.net/en-us'
    html = get_html(url)
    if html:
        get_links(html)
    else:
        print("Failed to retrieve HTML.")