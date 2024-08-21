import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



with open(r'config.json', 'r') as json_file :
    data = json.load(json_file)




# Set the path to the Chromedriver
DRIVER_PATH = '/Users/rajkumar/PycharmProjects/TTDAutomation/chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service,options=options)

# Navigate to the URL
driver.get('https://ttdevasthanams.ap.gov.in/home/dashboard')
driver.implicitly_wait(1.2)
driver.find_element(By.XPATH, "//span[contains(text(), 'Log In')]").click()
driver.implicitly_wait(1.2)
driver.find_element(By.XPATH, "//form/div/div[1]/div[2]/div/input").send_keys("9952187489")
driver.implicitly_wait(1.2)
driver.find_element(By.XPATH, "//button[contains(text(), 'Get OTP')]").click()

def enter_input(data, element_name, element_type):
    rows = driver.find_elements(By.XPATH, f'//input[@label="{element_name}"]')
    if element_type.casefold() == "text":
        for idx, row in enumerate(rows):
            print(data[idx].get(element_name))
            row.send_keys(data[idx].get(element_name))
    else :
        # Process Dropdown
        for idx, row in enumerate(rows):
            # time.sleep(0.1)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(row)
            )
            row.click()
#             time.sleep(0.1)
            if element_name.casefold() == "gender".casefold() :
                if data[idx].get(element_name).casefold() == "male" :
                    driver.find_element(By.XPATH, '//li[contains(text(), "Male")]').click()

                else:
                    driver.find_element(By.XPATH, '//li[contains(text(), "Female")]').click()


            elif element_name.casefold() == "Photo ID Proof".casefold():
                if data[idx].get(element_name).casefold() == "aadhaar":
                    driver.find_element(By.XPATH, '//li[contains(text(), "Aadhaar")]').click()
                elif data[idx].get(element_name).casefold() == "passport":
                    driver.find_element(By.XPATH, '//li[contains(text(), "Passport")]').click()

#             time.sleep(0.1)

enter_input(data,"Name", "text")
enter_input(data,"Age", "text")
enter_input(data,"Gender", "")
enter_input(data,"Photo ID Proof", "")
enter_input(data,"Photo Id Number", "text")

driver.quit()