import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByClass():
    def locate_by_class_demo(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://login.live.com/")
        driver.find_element(By.CLASS_NAME, "fui-Input__input").send_keys("test@test.com")
        #driver.find_element(By.TAG_NAME, "input").send_keys("test@test.com")
        #driver.find_element(By.XPATH,"//button[normalize-space()='Siguiente']").click()
        #driver.find_element(By.ID, "login").click()

        next_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Siguiente']"))
        )
        next_button.click()

    time.sleep(5)

findById = DemoFindElementByClass()
findById.locate_by_class_demo()