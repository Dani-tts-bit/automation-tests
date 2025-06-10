import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class demoHiddenElement():
    def demo_is_displayed(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "(//div[@id='myDIV'])[1]").is_displayed()

        print(elem)

        time.sleep(5)


        driver.find_element(By.XPATH, "(//button[normalize-space()='Toggle Hide and Show'])[1]").click()

        elem2 = driver.find_element(By.XPATH, "(//button[normalize-space()='Toggle Hide and Show'])[1]").is_displayed()


        print(elem2)



        time.sleep(5)


    def demo_is_displayed_yatra(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "(//div[@id='myDIV'])[1]").is_displayed()





demoisDisplayed = demoHiddenElement()
demoisDisplayed.demo_is_displayed()