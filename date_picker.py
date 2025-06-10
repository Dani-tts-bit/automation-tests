from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class demoAutosugest():
    def demo_autosugest(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://demoqa.com/date-picker")

        wait = WebDriverWait(driver, 10)

        # Espera a que el input sea visible
        calendar = wait.until(EC.visibility_of_element_located((By.ID, "datePickerMonthYearInput")))

        # Limpiamos el campo y escribimos la fecha en formato MM/DD/YYYY
        calendar.clear()
        calendar.send_keys("06/30/2021")
        calendar.send_keys(Keys.ENTER)

        time.sleep(3)  # Esperar unos segundos para ver el resultado
        driver.quit()


democalendar = demoAutosugest()
democalendar.demo_autosugest()
