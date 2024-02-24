from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://chat.openai.com/")

driver.implicitly_wait(10)

box = driver.find_element(by=By.ID, value="login-button")
box.click("Hello")

#text_box.send_keys("Hello")
# submit_button.click()

time.sleep(5)

# message = driver.find_element(by=By.ID, value="message")
# value = message.text
driver.quit()