from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
