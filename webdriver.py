# jobbot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://linkedin.com")

title = driver.title

driver.implicitly_wait(0.5)

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")
username.send_keys("sj2802@columbia.edu")
password.send_keys("U7MT=22Tp-T%.UY")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(0.5)
time.sleep(20)
driver.find_element(By.CSS_SELECTOR, "[href='https://www.linkedin.com/jobs/?']").click()
driver.implicitly_wait(0.5)

driver.get('https://www.linkedin.com/jobs/search?keywords=software%20engineer&location=United%20States')

job_block = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
jobs = job_block.find_elements(By.TAG_NAME, "li")
n = len(jobs)
f = open("demofile2.txt", "a")
i = 0

while i < n:
    driver.implicitly_wait(0.5)
    jobs = job_block.find_elements(By.TAG_NAME, "li")
    n = len(jobs)
    i += 1
    # f.write(str(len(jobs)) + '\n')
    if i < n:
        ActionChains(driver).double_click(jobs[i]).perform()
        driver.implicitly_wait(0.5)
        driver.switch_to.window(driver.window_handles[-1])
        d1 = driver.find_element(By.CLASS_NAME, "jobs-search__job-details--wrapper")
        d2 = d1.find_element(By.CLASS_NAME, "job-view-layout.jobs-details")
        d3 = d2.find_element(By.CLASS_NAME, "t-14")
        d4 = d3.find_element(By.CLASS_NAME, "mt5")
        d5 = d4.find_element(By.CLASS_NAME, "display-flex")
        d6 = d5.find_element(By.CLASS_NAME, "jobs-s-apply.jobs-s-apply--fadein.inline-flex.mr2")
        driver.implicitly_wait(0.5)
        try:
            #f.write("trying\n")
            #d7 = d6.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
           # d6.find_element(By.XPATH, "//button").click()
            #button = d6.find_element(By.CLASS_NAME, "jobs-apply-button.artdeco-button.artdeco-button--icon-right.artdeco-button--3 artdeco-button--primary.ember-view")
           # button.click()
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(.)='Apply']"))).click()
            f.write('button clicked\n')
            time.sleep(5)
        except:
            f.write('continue\n')
            continue

         #find_element(By.CSS_SELECTOR, "[href='#link-external-small']").click())

      #  ActionChains(driver).double_click(d5.find_element(By.XPATH)).perform()

    #wait = WebDriverWait(driver, 100)
    #element = wait.until(EC.element_to_be_clickable(jobs[i]))
    # element.click()
    driver.implicitly_wait(0.5)
# driver.find_element(By.XPATH, "//button[@text()='Apply']").click()
#  e2 = wait.until(EC.element_to_be_clickable(By.CLASS_NAME, "scaffold-layout__list-detail-container"))

# applyButton = driver.find_elements(By.XPATH, "//button[@type='submit']")
#if len(applyButton) > 0:
# applyButton[0].click()

#jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, ".jobs-search-resultsw__list-item")

time.sleep(10)

#driver.implicitly_wait(1000000)
#driver.quit()
