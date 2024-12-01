from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
time.sleep(0.1)
driver.execute_script("window.scrollBy(0, 350);")

Home_open = driver.find_element(By.CSS_SELECTOR, '.rct-icon.rct-icon-expand-close')
Home_open.click()
print('Home opened')
time.sleep(0.2)
Downloads_open = driver.find_element(By.CSS_SELECTOR, 'li:nth-child(3) span:nth-child(1) button:nth-child(1) svg')
Downloads_open.click()
print('Downloads opened')
time.sleep(0.2)
Exel_check = driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-excelFile'] span[class='rct-checkbox'] svg")
Exel_check.click()
print('Exel Clicked')
time.sleep(0.2)
Documents_check = driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-documents'] span[class='rct-checkbox'] svg")
Documents_check.click()
print('Documents Clicked')
time.sleep(0.2)
result = driver.find_element(By.CSS_SELECTOR, "div[id='result'] span:nth-child(1)")
print(result.text)
assert result.text == "You have selected :"

time.sleep(3)
print('Script quited successfully')
driver.quit()
