import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class DemoSeleniumLearning():
    def demo_browser_methods(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://training.rcvacademy.com")

        driver.find_element(By.XPATH, "(//input[@id='email'])[1]").send_keys("pepe@gmail.com")
        time.sleep(5)


demobrowser = DemoSeleniumLearning()
demobrowser.demo_browser_methods()