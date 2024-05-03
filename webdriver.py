# jobbot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Chrome()
driver.get("https://linkedin.com")

title = driver.title

driver.implicitly_wait(0.5)

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")
username.send_keys("sj2802@columbia.edu")
password.send_keys("")


driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(0.5)
time.sleep(20)
driver.find_element(By.CSS_SELECTOR, "[href='https://www.linkedin.com/jobs/?']").click()
driver.implicitly_wait(0.5)

driver.get('https://www.linkedin.com/jobs/search?keywords=software%20engineer&location=United%20States')

job_block = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
jobs = job_block.find_elements(By.TAG_NAME, "li")
driver.implicitly_wait(3.0)

for job in jobs:
   # d1 = job.find_element(By.XPATH, "//div[@data-view-name='job-card']")
    #d2 = d1.find_element(By.CLASS_NAME, "full-width artdeco-entity-lockup__title ember-view")
    #link = d2.find_element(By.CLASS_NAME, 'disabled ember-view job-card-container__link job-card-list__title job-card-list__title--link')
    #link.click()
    #f.write("Now the file has more content!")
   #ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
  # your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
   #   .until(expected_conditions.presence_of_element_located(job))
   #ActionChains(driver).move_to_element(job).click().perform()
   ActionChains(driver).double_click(job).perform()
   driver.implicitly_wait(0.5)
   # applyButton = driver.find_elements(By.XPATH, "//button[@type='submit']")
    #if len(applyButton) > 0:
       # applyButton[0].click()

#jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

time.sleep(10)

#driver.implicitly_wait(1000000)
#driver.quit()