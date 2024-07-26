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

# ____________________

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Запуск браузера
# driver = webdriver.Chrome()

# # Ожидание 10 секунд
# time.sleep(10)

# # Переход на сайт
# driver.get("https://capstroy.kg/")

# # Ожидание 5 секунд, чтобы страница полностью загрузилась
# time.sleep(5)

# # Поиск кнопки по указанному классу и нажатие на нее
# callback_button = driver.find_element(By.CSS_SELECTOR, ".callback-head.d-lg-flex.d-none.nav-hover")
# callback_button.click()

# # Ожидание появления текстового поля
# time.sleep(2)  # Можно заменить на WebDriverWait для более надежного ожидания

# # Поиск текстового поля по классу и ввод текста
# textarea = driver.find_element(By.CSS_SELECTOR, ".feedbackInput.nameInput")
# textarea.send_keys("Распакрука Нй!")
# time.sleep(5)

# textarea = driver.find_element(By.CSS_SELECTOR, ".feedbackInput.phoneInput")
# textarea.send_keys("+996700232322")
# time.sleep(5)

# # Закрытие браузера
# driver.quit()
