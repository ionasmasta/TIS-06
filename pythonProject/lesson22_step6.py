from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

x = browser.find_element(By.XPATH,'//*[@id="input_value"]')
x = x.text
y = calc(x)
print(y)

browser.execute_script("window.scrollBy(0, 100);")
import1 = browser.find_element(By.XPATH,'//*[@id="answer"]')
import1.send_keys(y)

button = browser.find_element(By.TAG_NAME,'button')

import2 = browser.find_element(By.XPATH,'//*[@id="robotCheckbox"]')
import2.click()

import3 = browser.find_element(By.XPATH,'//*[@id="robotsRule"]')
import3.click()

import4 = browser.find_element(By.XPATH, '/html/body/div/form/button')
import4.click()


time.sleep(10)
browser.quit()