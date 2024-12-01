from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")
time.sleep(0.1)

Radio_yes = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
Radio_yes.click()
print('Radio YES clicked')
result = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert result.text == "Yes"

time.sleep(0.2)
Radio_Impressive = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
Radio_Impressive.click()
print('Radio Impressive clicked')
result = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert result.text == "Impressive"

time.sleep(0.2)
Radio_no = driver.find_element(By.XPATH, "//label[@for='noRadio']")
Radio_no.click()
print('Radio NO clicked')
result = driver.find_element(By.XPATH, "//span[@class='text-success']")
assert result.text == "Impressive"

time.sleep(3)
print('Script quited successfully')
driver.quit()
