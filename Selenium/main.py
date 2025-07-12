import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("TARGET_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def type_safely(input_element, text, delay=0.1):
    for char in text:
        input_element.send_keys(char)
        time.sleep(delay)
        current_value = input_element.get_attribute("value")
        if not current_value.endswith(char):
            input_element.send_keys(char)
            time.sleep(delay)

driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 20)

username_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
username_input.click()
username_input.clear()
type_safely(username_input, username)

password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
password_input.click()
password_input.clear()
type_safely(password_input, password)

password_input.send_keys(Keys.RETURN)

try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//nav")))
    print("✅ Logged in successfully!")
except:
    print("⚠️ Login may have failed or additional steps required (captcha, 2FA).")

input("Press ENTER to close the browser...")
driver.quit()