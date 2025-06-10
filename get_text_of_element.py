import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetText():
    def demo_text_method(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://training.rcvacademy.com")

        text = driver.find_element(By.XPATH, "(//p[@class='margin-top-10 margin-bottom-10 None dynamic-text'])[1]").text
        time.sleep(5)
        print(text)


demotext = DemoGetText()
demotext.demo_text_method()