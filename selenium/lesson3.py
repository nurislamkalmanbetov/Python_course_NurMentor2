import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера
driver = webdriver.Chrome()

# Переход на сайт с текущей стоимостью биткоина
driver.get("https://www.coindesk.com/price/bitcoin")

# Ожидание загрузки страницы
time.sleep(5)

# Клик по кнопке согласия с куками
cookie_button = driver.find_element(By.ID, ".CybotCookiebotDialogBodyButtonAccept")
cookie_button.click()

# Ожидание после клика по кнопке
time.sleep(2)

# Поиск элемента с текущей стоимостью биткоина
price_element = driver.find_element(By.CLASS_NAME, ".currency-pricestyles__Price-sc-1v249sx-0.fcfNRE")
bitcoin_price = price_element.text

# Сохранение стоимости биткоина в файл
with open("bitcoin_price.txt", "w") as file:
    file.write(f"Текущая стоимость биткоина: {bitcoin_price}")

# Закрытие браузера
driver.quit()
