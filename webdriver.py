# jobbot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://linkedin.com")


title = driver.title

driver.implicitly_wait(0.5)

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")
username.send_keys("sj2802@columbia.edu")
password.send_keys("")

"""
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text()
"""
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(0.5)
driver.find_element(By.CSS_SELECTOR, "[href='https://www.linkedin.com/jobs/?']").click()
driver.implicitly_wait(0.5)

driver.get('https://www.linkedin.com/jobs/search?keywords=software%20engineer&location=United%20States')
time.sleep(100)

#driver.implicitly_wait(1000000)
#driver.quit()