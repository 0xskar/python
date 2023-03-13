from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.python.org/")

# TODO Collect Upcomming Events from python.org and store in a dictionary.
events_table = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")
events_to_format = [event.text for event in events_table]

event_dict = {}

for i, event in enumerate(events_to_format):
    data = event.split('\n')
    event_dict.update({
        f"{i}": {
            "time": data[0],
            "name": data[1]
        }
    })

print(event_dict)
driver.close()
