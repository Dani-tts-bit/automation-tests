import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class demoRadioButtons():
    def demo_radiobuttons(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://designsystem.digital.gov/components/radio-buttons/")
        driver.find_element(By.XPATH, "(//label[normalize-space()='Frederick Douglass'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//label[@for='historical-washington']").click()

        time.sleep(3)

demoradiobuttons = demoRadioButtons()
demoradiobuttons.demo_radiobuttons()