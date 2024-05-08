import requests
from bs4 import BeautifulSoup as BS 

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None 


def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_='container-fluid my-3x md:my-4x')
    posts = container.find_all('a', class_='p-2x flex flex-col gap-y-2x')
    print(posts)
    for post in posts:
        prices = post.find('div', class_='flex gap-x-0.5x')
        price = prices.find('span', class_='whitespace-nowrap text-title_4').text.strip().replace(" ", "")
        price_m2 = prices.find('p', class_='text-gray__dark_1 whitespace-nowrap text-caption').text.strip()
        title = post.find('p', class_='whitespace-nowrap truncate text-body_2').text.strip()
        location = post.find('p', class_='whitespace-nowrap text-gray__dark_2 truncate text-caption').text.strip()
        print(
            f'Цена {price} \n', 
            f'Цена кв метр {price_m2} \n', 
            f'Описание {title} \n', 
            f'Место {location} \n'
            )




def main():
    URL = 'https://aqarmap.com.eg/en/for-sale/property-type/cairo/new-cairo/'
    html = get_html(URL)
    get_data(html)
    
    
if __name__ == '__main__':
    main()