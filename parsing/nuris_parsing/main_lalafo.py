import requests
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):

    soup = BS(html, 'html.parser')
    tabs = soup.find('div', class_='container-xl')
    posts = tabs.find_all('article', class_='lf-ad-tile')

    # print(posts)

    links = []
    for post in posts: 
        title = post.find('a', class_='lf-ad-tile__link').text.strip()
        price_element = post.find('span', class_='LFCaption size-12 ad-tile-price ad-tile-price__old')
        price = price_element.get_text(strip=True) if price_element else "Цена не указана"
        picture = post.find('img')['src']
        
        links.append((title, price, picture))

    return links



def main():
    URL = 'https://lalafo.kg/'
    html = get_html(URL)
    if html:
        links = get_links(html)
        for title, price, picture in links:
            print(f"Заголовок: {title}\nЦена: {price}\nКартинка: {picture}")
    else:
        print("Не удалось получить HTML-страницу")

if __name__ == '__main__':
    main()