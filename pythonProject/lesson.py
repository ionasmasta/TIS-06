import time #Импортируем библиотеку time. Для использования пауз.
from selenium import webdriver # Импортируем библиотеку веб-драйвера
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome() # Открываем бразуер хром
driver.get('https://www.saucedemo.com/') # Переходим по ссылке
driver.maximize_window() # Расширяем окно на полный экран

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') # Находим поле для ввода логина на сайте через chrome консоль методом Xpath, наведя курсор и кликнув правой кнопкой мыши и скопировать xpath
user_name.send_keys("standard_user") # вводим логин

password = driver.find_element(By.CSS_SELECTOR, "#password") # Находим поле ввода пароля
password.send_keys('secret_sauce') # Вводим пароль

button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]') # Находим элемент с кнопкой
button_login.click() # Нажимаем на кнопку

time.sleep(10) # Включаем паузу на 10 секунд
driver.close # Закрываем окно бразуера