import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class demoCheckBoxes():
    def demo_checkbox(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.sugarcrm.com/es/request-demo/")
        driver.find_element(By.CSS_SELECTOR, "label[for='input_1_12_1']").click()
        var1 = driver.find_element(By.CSS_SELECTOR, "label[for='input_1_12_1']").is_selected()
        print(var1)

        time.sleep(3)

democheckboxes = demoCheckBoxes()
democheckboxes.demo_checkbox()