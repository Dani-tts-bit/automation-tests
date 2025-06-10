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
        driver.get("https://www.laserairlines.com/")

        wait = WebDriverWait(driver, 20)

        # Aceptar cookies si aparecen
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_cookies.click()
        except:
            pass

        # Verificar si hay iframes y buscar el campo "Origen"
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"Cantidad de iframes encontrados: {len(iframes)}")

        origin_found = False
        for index, iframe in enumerate(iframes):
            driver.switch_to.default_content()
            driver.switch_to.frame(iframe)
            try:
                origin_input = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Origen']"))
                )
                origin_input.click()
                origin_input.send_keys("Caracas")
                origin_input.send_keys(Keys.ENTER)
                print(f"¡Campo de origen encontrado en iframe {index}!")
                origin_found = True
                break
            except:
                print(f"No se encontró el campo 'Origen' en iframe {index}")
                continue

        if origin_found:
            driver.switch_to.default_content()
            for index, iframe in enumerate(iframes):
                driver.switch_to.frame(iframe)
                try:
                    destination_input = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Destino']"))
                    )
                    destination_input.click()
                    destination_input.send_keys("Barcelona")
                    destination_input.send_keys(Keys.ENTER)
                    print(f"¡Campo de destino encontrado en iframe {index}!")
                    break
                except:
                    print(f"No se encontró el campo 'Destino' en iframe {index}")
                    continue
        else:
            print("No se pudo encontrar el campo de origen en ningún iframe.")

        time.sleep(5)
        driver.quit()

autosugestion = demoAutosugest()
autosugestion.demo_autosugest()




