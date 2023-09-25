#Импорт библиотек***
from selenium import webdriver # Импортируем библиотеку веб-драйвера
from selenium.webdriver.common.by import By # Импортируем библиотеку By
import time #Импортируем библиотеку time
import math

link = "http://suninjuly.github.io/find_link_text"  #Создаем переменную по ссылке

try:
    browser = webdriver.Chrome() # Открываем Chrome
    browser.get(link) # Переходим по ссылке указанной в переменной link

  x = str(math.ceil(math.pow(math.pi, math.e)*10000))
  a1 = browser.find_element(By.LINK_TEXT, x)
  a1.click()
input1 = browser.find_element(By.TAG_NAME, 'input')  # Находим поле для ввода firstname
input1.send_keys("Ivan")  # вводим Ivan
input2 = browser.find_element(By.NAME, 'last_name')  # Находим поле для ввода lastname
input2.send_keys("Petrov")  # вводим Petrov
input3 = browser.find_element(By.CLASS_NAME, 'city')  # Находим поле для ввода города
input3.send_keys("Smolensk")  # вводим Smolensk
input4 = browser.find_element(By.ID, "country")  # Находим поле для ввода страны
input4.send_keys("Russia")  # вводим Россия
button = browser.find_element(By.CSS_SELECTOR, "button.btn")  # Находим кнопку
button.click()  # нажимаем кнопку

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10) #пауза 10 секунд
    # закрываем браузер после всех манипуляций
    browser.quit() #закрываем окно браузера

# не забываем оставить пустую строку в конце файла