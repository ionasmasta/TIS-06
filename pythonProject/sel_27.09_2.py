'''Импорт библиотек'''
import time #Импортируем библиотеку time. Для использования пауз.
from selenium import webdriver # Импортируем библиотеку веб-драйвера
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()

driver.get('https://stepik.org/catalog')
driver.maximize_window()

time.sleep(3)
login = driver.find_element(By.XPATH, '//*[@id="ember245"]')
login.click()

user_name = driver.find_element(By.XPATH, '//*[@id="id_login_email"]')
user_name.send_keys('ionas0988@gmail.com')

password = driver.find_element(By.XPATH, '//*[@id="id_login_password"]')
password.send_keys('27112711i')

button_login = driver.find_element(By.XPATH, '//*[@id="login_form"]/button')
button_login.click()

time.sleep(5)
driver.close