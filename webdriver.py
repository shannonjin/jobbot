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


def greenhouse(driver):
    driver.find_element(By.ID, 'first_name').send_keys("Shannon")
    driver.find_element(By.ID, 'last_name').send_keys("Jin")
    driver.find_element(By.ID, 'email').send_keys("sj2802@columbia.edu")
    driver.find_element(By.ID, 'phone').send_keys("2405055041")
    driver.find_element(By.ID, 'job_application_answers_attributes_0_text_value').send_keys(
        'https://www.linkedin.com/in/shannon-jin-a7580178/')
    driver.find_element(By.ID, 'job_application_answers_attributes_1_text_value').send_keys('https://github.com/shannonjin')
    resume_file = '/Users/shannonj/Documents/JHS/new_generic_3/shannonJinResume.pdf'
    driver.find_element(By.CSS_SELECTOR, "[aria-describedby='resume-allowable-file-types']").send_keys(resume_file)
    driver.find_element(By.ID, "file-submit").click()

    #wait = WebDriverWait(driver, 5)
   # ele = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="s3_upload_for_resume" and @type="file"]')))
   # ele = wait.until(EC.presence_of_element_located((By.ID, "s3_upload_for_resume")))
   # ele.send_keys(resume_file)
    '''
    try:
        cover_letter_file = '/Users/shannonj/Documents/JHS/new_generic_3/shannonJinCoverLetter.pdf'
        eli = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="s3_upload_for_cover_letter" and @type="file"]')))
        eli.send_keys(cover_letter_file)
    except:
        print('dang')
    '''
    time.sleep(100)


driver = webdriver.Chrome()
driver.get("https://linkedin.com")

title = driver.title

driver.implicitly_wait(0.5)

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")
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
        try:
            WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(.)='Apply']"))).click()
            driver.switch_to.window(driver.window_handles[1])
            url = str(driver.current_url)
            if 'greenhouse' in url:
                greenhouse(driver)
          #  elif 'lever' in url:
            # #elif 'myworkdayjobs' in url:


            time.sleep(100)
        except:
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
