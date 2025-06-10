import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByID():
    def locate_by_id_demo(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://login.live.com/")

        try:
            # Esperar explícitamente hasta que el campo de correo esté visible (máx 15 seg)
            email_input = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.ID, "usernameEntry"))
            )
            email_input.send_keys("test@test.com")
        except Exception as e:
            print("Error localizando el elemento:", e)
    time.sleep(10)

findById = DemoFindElementByID()
findById.locate_by_id_demo()


