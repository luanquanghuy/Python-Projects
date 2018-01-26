from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://lmgtfy.com/")
print("Opened Google")
key = driver.find_element(By.XPATH, '//button[text()="Get Link"]')
key.click()
button = driver.find_element_by_class_name("btn btn-primary btn-lg")
button.click()
print("FB opened")
# 2 3 1
# 3 5 2
# 1 2 7