import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера
driver = webdriver.Chrome()

# Ожидание 10 секунд
time.sleep(10)

# Переход на сайт
driver.get("https://capstroy.kg/")

# Ожидание 5 секунд, чтобы страница полностью загрузилась
time.sleep(5)

# Поиск кнопки по указанному классу и нажатие на нее
callback_button = driver.find_element(By.CSS_SELECTOR, ".callback-head.d-lg-flex.d-none.nav-hover")
callback_button.click()

# Ожидание 5 секунд
time.sleep(5)

# Закрытие браузера
driver.quit()
