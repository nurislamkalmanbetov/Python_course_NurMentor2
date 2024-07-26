import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://www.coindesk.com/price/bitcoin/")
time.sleep(13)

cookie_button = driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonAccept")
cookie_button.click()
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".currency-pricestyles__Price-sc-1v249sx-0.fcfNRE").text

with open('bitcoin.txt', 'w') as x:
        x.write(textarea)

time.sleep(5)

driver.quit()
