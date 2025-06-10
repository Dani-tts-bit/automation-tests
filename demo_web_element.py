import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetAtributte():
    def demo_atributte_method(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://training.rcvacademy.com")

        attr_value = driver.find_element(By.XPATH, "(//a[normalize-space()='Get Access'])[1]").get_attribute("data-lists")
        print(attr_value)

        time.sleep(5)


demoatributte = DemoGetAtributte()
demoatributte.demo_atributte_method()