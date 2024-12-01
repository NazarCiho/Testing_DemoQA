from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
actions = ActionChains(driver)
time.sleep(0.1)
driver.execute_script("window.scrollBy(0, 250);")

def sorting():
    # Sorting rows
    driver.find_element(By.XPATH, "//div[contains(text(),'First Name')]").click()
    time.sleep(0.2)
    results = driver.find_elements(By.XPATH, "//*[@class='rt-td']")
    result = results[0]
    assert result.text == "Alden"
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//div[contains(text(),'Age')]").click()
    results = driver.find_elements(By.XPATH, "//*[@class='rt-td']")
    result = results[2]
    assert result.text == "29"
    return '✅ SORTING was successful'
def edit_AND_delete():
    # Deleting row
    driver.find_element(By.XPATH, "//span[@id='delete-record-3']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]").click()
    time.sleep(0.5)
    # Editing row
    driver.find_element(By.XPATH,"//span[@id='edit-record-1']//*[name()='svg']").click()
    time.sleep(0.2)
    first_name=driver.find_element(By.XPATH,"//input[@id='firstName']")
    first_name.click()
    first_name.send_keys('Edited name')
    time.sleep(0.2)
    driver.find_element(By.XPATH,"//button[@id='submit']").click()
    time.sleep(1)
    return '✅ EDIT_AND_DELETE was successful'
def adding():
    # Adding a new row
    driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']").click()
    input_list = {'firstName': 'Nazar', 'lastName': 'Tsikhotskyi', 'userEmail': 'nazar@gmail.com', 'age': 52, 'salary': 1488, 'department': 'software'}
    for inp in input_list.keys():
        item = driver.find_element(By.XPATH, f"//input[@id='{inp}']")
        item.click()
        item.send_keys(input_list[inp])
        time.sleep(0.1)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    return '✅ ADDING was successful'
def search():
    search_box = driver.find_element(By.XPATH,"//input[@id='searchBox']")
    search_box.click()
    time.sleep(0.5)
    search_box.send_keys('Nazar')
    results = driver.find_elements(By.XPATH, "//*[@class='rt-td']")
    result = results[0]
    assert result.text == "Nazar"
    return '✅ Search was successful'
if __name__ == '__main__':
    print(sorting())
    print(edit_AND_delete())
    print(adding())
    print(search())
    time.sleep(3)
    print('Script quited successfully')
    driver.quit()
