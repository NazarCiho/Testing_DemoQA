import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


def test_bosco():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com.ua/")
    time.sleep(0.5)
    google_search_input = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
    google_search_input.click()
    google_search_input.send_keys('Bosco Lviv')
    google_search_input.send_keys(Keys.RETURN)
    time.sleep(0.1)
    first_result = driver.find_elements(By.CSS_SELECTOR, 'h3')[0]
    first_result.click()

    result = driver.find_element(By.CSS_SELECTOR, '.study_title')
    assert result.text == "ПЕРЕВАГИ НАВЧАННЯ"
    time.sleep(0.1)
    print('Script quited successfully')
    driver.quit()

def test_TextBox_XPATH():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 400);")
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
    print('Script quited successfully')
    driver.quit()

def test_CheckBox_XPATH():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 350);")

    Home_open = driver.find_element(By.XPATH, "//button[@title='Toggle']//*[name()='svg']")
    Home_open.click()
    print('Home opened')
    time.sleep(0.2)
    Downloads_open = driver.find_element(By.XPATH, "//li[3]//span[1]//button[1]//*[name()='svg']")
    Downloads_open.click()
    print('Downloads opened')
    time.sleep(0.2)
    Exel_check = driver.find_element(By.XPATH,
                                     "//label[@for='tree-node-excelFile']//span[@class='rct-checkbox']//*[name()='svg']")
    Exel_check.click()
    print('Exel Clicked')
    time.sleep(0.2)
    Documents_check = driver.find_element(By.XPATH,
                                          "//label[@for='tree-node-documents']//span[@class='rct-checkbox']//*[name()='svg']")
    Documents_check.click()
    print('Documents Clicked')
    time.sleep(0.2)
    result = driver.find_element(By.XPATH, "//span[normalize-space()='You have selected :']")
    assert result.text == "You have selected :"
    print('Script quited successfully')
    driver.quit()
def test_RadioButton_XPATH():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 250);")
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
    print('Script quited successfully')
    driver.quit()
def test_Webtables_XPATH():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    actions = ActionChains(driver)
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 250);")

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

    # Deleting row
    driver.find_element(By.XPATH,
                        "//span[@id='delete-record-3']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]").click()
    time.sleep(0.5)
    # Editing row
    driver.find_element(By.XPATH, "//span[@id='edit-record-1']//*[name()='svg']").click()
    time.sleep(0.2)
    first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
    first_name.click()
    first_name.send_keys('Edited name')
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(1)

    # Adding a new row
    driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
    input_list = {'firstName': 'Nazar', 'lastName': 'Tsikhotskyi', 'userEmail': 'nazar@gmail.com', 'age': 52,
                  'salary': 1488, 'department': 'software'}
    for inp in input_list.keys():
        item = driver.find_element(By.XPATH, f"//input[@id='{inp}']")
        item.click()
        item.send_keys(input_list[inp])
        time.sleep(0.1)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()

    search_box = driver.find_element(By.XPATH, "//input[@id='searchBox']")
    search_box.click()
    time.sleep(0.5)
    search_box.send_keys('Nazar')
    results = driver.find_elements(By.XPATH, "//*[@class='rt-td']")
    result = results[0]
    assert result.text == "Nazar"
    print('Script quited successfully')
    driver.quit()


def test_Buttons_XPATH():
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
    print('Script quited successfully')
    driver.quit()
def test_TextBox_CSS():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 400);")

    FullName = driver.find_element(By.CSS_SELECTOR, '#userName')
    FullName.click()
    FullName.send_keys('My Test Name?')
    print('Full Name sented')
    time.sleep(0.2)
    Email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    Email.click()
    Email.send_keys('example@gmail.yt')
    print('Email sented')
    time.sleep(0.2)
    CurrentAddress = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    CurrentAddress.click()
    CurrentAddress.send_keys('Adress, 14 street')
    print('Current adress sented')
    time.sleep(0.2)
    permanentAddress = driver.find_element(By.CSS_SELECTOR, '#permanentAddress')
    permanentAddress.click()
    permanentAddress.send_keys('New Adress street')
    print('Permanent adress sented')
    time.sleep(0.2)
    Submit = driver.find_element(By.CSS_SELECTOR, '#submit')
    Submit.click()
    print('Submit button clicked')
    time.sleep(0.2)

    result = driver.find_element(By.CSS_SELECTOR, '.border.col-md-12.col-sm-12')
    assert result.text == "Name:My Test Name?\nEmail:example@gmail.yt\nCurrent Address :Adress, 14 street\nPermananet Address :New Adress street"
    print('Script quited successfully')
    driver.quit()

def test_CheckBox_CSS():
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
    Documents_check = driver.find_element(By.CSS_SELECTOR,
                                          "label[for='tree-node-documents'] span[class='rct-checkbox'] svg")
    Documents_check.click()
    print('Documents Clicked')
    time.sleep(0.2)
    result = driver.find_element(By.CSS_SELECTOR, "div[id='result'] span:nth-child(1)")
    print(result.text)
    assert result.text == "You have selected :"
    print('Script quited successfully')
    driver.quit()

def test_RadioButton_CSS():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 250);")

    Radio_yes = driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
    Radio_yes.click()
    print('Radio YES clicked')
    result = driver.find_element(By.CSS_SELECTOR, ".text-success")
    assert result.text == "Yes"

    time.sleep(0.2)
    Radio_Impressive = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
    Radio_Impressive.click()
    print('Radio Impressive clicked')
    result = driver.find_element(By.CSS_SELECTOR, ".text-success")
    assert result.text == "Impressive"

    time.sleep(0.2)
    Radio_no = driver.find_element(By.CSS_SELECTOR, "label[for='noRadio']")
    Radio_no.click()
    print('Radio NO clicked')
    result = driver.find_element(By.CSS_SELECTOR, ".text-success")
    assert result.text == "Impressive"
    print('Script quited successfully')
    driver.quit()

def test_Webtables_CSS():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    actions = ActionChains(driver)
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 280);")

    # Sorting rows
    driver.find_element(By.CSS_SELECTOR, "div[role='row'] div:nth-child(1) div:nth-child(1)").click()
    time.sleep(0.2)
    results = driver.find_elements(By.CSS_SELECTOR, ".rt-td")
    result = results[0]
    assert result.text == "Alden"
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, "div[class='rt-thead -header'] div:nth-child(3) div:nth-child(1)").click()
    results = driver.find_elements(By.CSS_SELECTOR, ".rt-td")
    result = results[2]
    assert result.text == "29"

    # Deleting row
    driver.find_element(By.CSS_SELECTOR, "span[id='delete-record-3'] svg path").click()
    time.sleep(0.5)
    # Editing row
    driver.find_element(By.CSS_SELECTOR, "span[id='edit-record-1'] svg path").click()
    time.sleep(0.2)
    first_name = driver.find_element(By.CSS_SELECTOR, "#firstName")
    first_name.click()
    first_name.send_keys('Edited name')
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, "#submit").click()
    time.sleep(1)

    # Adding a new row
    driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton").click()
    input_list = {'firstName': 'Nazar', 'lastName': 'Tsikhotskyi', 'userEmail': 'nazar@gmail.com', 'age': 52,
                  'salary': 1488, 'department': 'software'}
    for inp in input_list.keys():
        item = driver.find_element(By.CSS_SELECTOR, f"#{inp}")
        item.click()
        item.send_keys(input_list[inp])
        time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, "#submit").click()

    search_box = driver.find_element(By.CSS_SELECTOR, "#searchBox")
    search_box.click()
    time.sleep(0.5)
    search_box.send_keys('Nazar')
    results = driver.find_elements(By.CSS_SELECTOR, ".rt-td")
    result = results[0]
    assert result.text == "Nazar"

    print('Script quited successfully')
    driver.quit()

def test_Buttons_CSS():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 400);")

    Click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    Click_me.click()
    print('One click clicked')
    result = driver.find_element(By.CSS_SELECTOR, "#dynamicClickMessage")
    assert result.text == "You have done a dynamic click"

    time.sleep(0.2)
    Rigth_Click_me = driver.find_element(By.CSS_SELECTOR, "#rightClickBtn")
    print('Right button GETTED')
    actions.context_click(Rigth_Click_me).perform()
    print('Right Click clicked')
    result = driver.find_element(By.CSS_SELECTOR, "#rightClickMessage")
    assert result.text == "You have done a right click"

    time.sleep(0.2)
    Double_click_me = driver.find_element(By.CSS_SELECTOR, "#doubleClickBtn")
    actions.double_click(Double_click_me).perform()
    print('Double click clicked')
    result = driver.find_element(By.CSS_SELECTOR, "#doubleClickMessage")
    assert result.text == "You have done a double click"
    print('Script quited successfully')
    driver.quit()