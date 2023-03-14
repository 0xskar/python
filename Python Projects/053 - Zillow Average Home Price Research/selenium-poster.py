from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import json
import time

data = "data.json"


class FormPoster:
    def __init__(self, form_data):
        self.FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfwa6dHnxR_F9E2M0dMKq3J7S-tIn50tIMUWQ3EA4jvb7yWJA/viewform"
        self.d = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.housing_data = []
        with open(form_data, mode="r") as file:
            # Convert file back to json
            # Remove newline from each line
            for line in file:
                line = line.strip()
                # Convert to a dictionary and append to housing_data
                item = json.loads(line)
                self.fill_out_form(url=item['url'], address=item['address'], footage=item['space'], price=item['price'])
                self.housing_data.append(item)

    def fill_out_form(self, url, address, footage, price):
        self.d.get(self.FORM_URL)
        time.sleep(2)
        print("Inserting Data: ", url, price, footage, address)
        url_input = self.d.find_element(By.XPATH,
                                        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_input = self.d.find_element(By.XPATH,
                                        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        footage_input = self.d.find_element(By.XPATH,
                                        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_input = self.d.find_element(By.XPATH,
                                        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
        submit_button = self.d.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        url_input.send_keys(url)
        address_input.send_keys(address)
        footage_input.send_keys(footage)
        price_input.send_keys(price)
        submit_button.click()



form_poster = FormPoster(data)
