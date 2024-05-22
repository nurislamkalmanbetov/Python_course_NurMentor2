import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='category-block sell')
    posts = container.find_all('div', class_='category-block-content-item')

    links = []
    for post in posts:
        link = post.get('href')
        full_link = 'https://www.house.kg/'+ link
        links.append(full_link)
    return links 

def get_data(html):
    soup = BS(html,'html.parser')
    container = soup.find('div', class_='main-content')
    posts = container.find_all('div',class_='details-header')

    title = posts.find('h1').text.strip()
    location = posts.find('div', class_='address').text.strip()
    price = posts.find('div',class_='price-dollar')

    data  = {
        'title' :title,
        'location' :location,
        'price':price,
        
    }
    return data

def main():
    URL = 'https://www.house.kg/details/4941641664a3d5c92a589-19000614'
    html = get_html(URL)
    if html:
        links = get_data(html)
    else:
        print('no')

    

if __name__ == '__main__':
    main()
