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

        calendar = wait.until(EC.presence_of_element_located((By.ID, "datePickerMonthYearInput")))

        # Elimina anuncios que puedan bloquear
        driver.execute_script("""
            var ads = document.querySelectorAll("iframe, .ad, .adsbygoogle");
            ads.forEach(el => el.remove());
        """)

        # Opcional: scroll al input
        driver.execute_script("arguments[0].scrollIntoView(true);", calendar)

        # Sin click: directamente editar
        calendar.send_keys(Keys.CONTROL, "a")
        calendar.send_keys(Keys.DELETE)
        calendar.send_keys("06/30/2021")
        calendar.send_keys(Keys.ENTER)

        print("Fecha seleccionada:", calendar.get_attribute("value"))

        time.sleep(3)
        driver.quit()

democalendar = demoAutosugest()
democalendar.demo_autosugest()

