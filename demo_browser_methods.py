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
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(5)

        driver.fullscreen_window()
        time.sleep(5)

        driver.minimize_window()
        time.sleep(5)

        driver.refresh()
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(5)

        driver.back()
        time.sleep(5)

        driver.forward()
        time.sleep(5)
        driver.quit()
        time.sleep(5)

demobrowser = DemoSeleniumLearning()
demobrowser.demo_browser_methods()