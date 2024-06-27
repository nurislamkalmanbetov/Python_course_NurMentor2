import time 

# Webdriver - набор команд для управления командами селениума 
from selenium import webdriver 

from selenium.webdriver.common.by import By

# инициализация драйвера
driver = webdriver.Chrome()

time.sleep(5)

# указываем браузеру куда и что нужно
driver.get("http://fortesters.easysmarthub.ru/form1")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".for-test_input")

# питон за нас напишет текст area get()
textarea.send_keys("Распакрука Нй!")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".for-test_button")

submit_button.click()
time.sleep(5)

driver.quit()