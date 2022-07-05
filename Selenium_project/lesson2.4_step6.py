from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(5)

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()

    text_ = browser.find_element(By.ID, "verify_message").text

    assert 'successful' in text_
    # Отправляем заполненную форму
    #browser.find_element(By.CLASS_NAME, "btn").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()