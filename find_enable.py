import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class demoelementstate():
    def demo_enable_disable(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://training.rcvacademy.com")

        #demo_estate = driver.find_element(By.XPATH, "(//a[normalize-space()='Get Access'])[1]").is_enabled()

        driver.find_element(By.XPATH, "input[@id='user_name']").send_keys("<EMAIL>")
        demoestate1 = driver.find_element(By.XPATH, "input[@id='user_pass']").send_keys("password")
        print(demoestate1)
        time.sleep(5)


demostate = demoelementstate()
demostate.demo_enable_disable()