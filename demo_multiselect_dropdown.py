import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class demoDropdownMultiSelect():
    def demo_dropdown(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://mdbootstrap.com/docs/standard/extended/multiselect/")
        driver.maximize_window()
        time.sleep(2)

        # Haz clic en el input para abrir el dropdown
        dropdown_input = driver.find_element(By.CSS_SELECTOR, "input.select-input.form-control")
        dropdown_input.click()
        time.sleep(1)

        # Selecciona opciones por texto visible
        # Opción "One"
        option_one = driver.find_element(By.XPATH, "//span[text()='One']")
        option_one.click()
        time.sleep(1)

        # Opción "Three"
        option_three = driver.find_element(By.XPATH, "//span[text()='Three']")
        option_three.click()
        time.sleep(1)

        # Puedes cerrar el dropdown si deseas haciendo clic afuera
        dropdown_input.click()
        time.sleep(3)

        driver.quit()

demodropdown = demoDropdownMultiSelect()
demodropdown.demo_dropdown()
