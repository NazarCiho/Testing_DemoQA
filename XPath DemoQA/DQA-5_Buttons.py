from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
actions = ActionChains(driver)
time.sleep(0.1)
driver.execute_script("window.scrollBy(0, 400);")

Click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
Click_me.click()
print('One click clicked')
result = driver.find_element(By.XPATH, "//p[@id='dynamicClickMessage']")
assert result.text == "You have done a dynamic click"

time.sleep(0.2)
Rigth_Click_me = driver.find_element(By.XPATH, "//button[text()='Right Click Me']")
actions.context_click(Rigth_Click_me).perform()
print('Right Click clicked')
result = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
assert result.text == "You have done a right click"

time.sleep(0.2)
Double_click_me = driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
actions.double_click(Double_click_me).perform()
print('Double click clicked')
result = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']")
assert result.text == "You have done a double click"
time.sleep(3)

print('Script quited successfully')
driver.quit()
