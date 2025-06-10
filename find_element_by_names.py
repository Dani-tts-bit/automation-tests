import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.microsoft.com/es-us/servicesagreement/")
        lista = driver.find_elements(By.TAG_NAME, ("div"))
        print(len(lista))
        #for i in lista:
            #print(i.text) #to print all the text associated to the link
#We can use this process to find the broken link on a page
findById = DemoFindElementByIDandName()
findById.locate_by_id_demo()