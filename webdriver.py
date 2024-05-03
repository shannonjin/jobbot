# jobbot
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get("https://linkedin.com")


title = driver.title

driver.implicitly_wait(0.5)

driver.find_element(By.XPATH,"//input[@name='session_key']")
driver.find_element(By.XPATH,"//input[@name='session_password']")

"""
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text()
"""
driver.implicitly_wait(30)
driver.quit()