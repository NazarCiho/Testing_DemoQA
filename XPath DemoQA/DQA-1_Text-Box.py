from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 380);")

FullName = driver.find_element(By.XPATH, "//input[@id='userName']")
FullName.click()
FullName.send_keys('My Test Name?')
print('Full Name sented')
time.sleep(0.2)
Email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
Email.click()
Email.send_keys('example@gmail.yt')
print('Email sented')
time.sleep(0.2)
CurrentAddress = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
CurrentAddress.click()
CurrentAddress.send_keys('Adress, 14 street')
print('Current adress sented')
time.sleep(0.2)
permanentAddress = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
permanentAddress.click()
permanentAddress.send_keys('New Adress street')
print('Permanent adress sented')
time.sleep(0.2)
Submit = driver.find_element(By.XPATH, "//button[@id='submit']")
Submit.click()
print('Submit button clicked')
time.sleep(0.2)

result = driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
assert result.text == "Name:My Test Name?\nEmail:example@gmail.yt\nCurrent Address :Adress, 14 street\nPermananet Address :New Adress street"

time.sleep(3)
print('Script quited successfully')
driver.quit()
