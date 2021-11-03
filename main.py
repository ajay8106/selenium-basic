import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"c:/selenium drivers"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com")

driver.implicitly_wait(3)
my_element=driver.find_element(By.ID,'mc-embedded-subscribe')
#my_element=driver.find_element_by_id('mc-embedded-subscribe')
my_element.click()

#sec_element = driver.find_element(By.ID,'esggu')

