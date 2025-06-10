import time
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class demoDropdwonSingleSelect():
    def demo_dropdown(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.rti.org/")
        dropdown = driver.find_element(By.NAME, "type")
        dd = Select(dropdown)

        dd.select_by_index(0)
        time.sleep(3)
        dd.select_by_value("/services-and-capabilities")
        time.sleep(3)

        dd.select_by_visible_text("Global Reach")
        time.sleep(3)


demodropdown = demoDropdwonSingleSelect()
demodropdown.demo_dropdown()