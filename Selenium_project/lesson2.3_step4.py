from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn").click()
    browser.switch_to.alert.accept()

    x = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(x)
    # browser.find_element(By.NAME, 'firstname').send_keys('firstname')
    # browser.find_element(By.NAME, 'lastname').send_keys('lastname')
    # browser.find_element(By.NAME, 'email').send_keys('email')

    # Отправляем заполненную форму
    browser.find_element(By.CLASS_NAME, "btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()