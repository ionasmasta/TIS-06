'''Импорт библиотек'''
import time #Импортируем библиотеку time. Для использования пауз.
from selenium import webdriver # Импортируем библиотеку веб-драйвера
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()
driver.get('https://stepik.org/catalog')
driver.maximize_window()

time.sleep(3)

search = driver.find_element(By.XPATH, '//*[@id="ember251"]/div/input')
search.send_keys('Python')

button = driver.find_element(By.XPATH, '//*[@id="ember248"]/div/button[3]')
button.click()

course = driver.find_element(By.XPATH, '//*[@id="ember1949"]/a[1]')
course.click()



time.sleep(40)
driver.close