from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('firstname')
    browser.find_element(By.NAME, 'lastname').send_keys('lastname')
    browser.find_element(By.NAME, 'email').send_keys('email')

    browser.find_element(By.ID, 'file').send_keys(file_path)

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