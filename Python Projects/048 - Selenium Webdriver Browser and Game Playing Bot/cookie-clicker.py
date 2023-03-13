from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

d = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
d.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

playing = True
while playing:

    # ELEMENTS
    cookie = d.find_element(By.ID, "cookie")
    time_machine = d.find_element(By.ID, "buyTime machine")
    portal = d.find_element(By.ID, "buyPortal")
    lab = d.find_element(By.ID, "buyAlchemy lab")
    shipment = d.find_element(By.ID, "buyShipment")
    mine = d.find_element(By.ID, "buyMine")
    factory = d.find_element(By.ID, "buyFactory")
    grandma = d.find_element(By.ID, "buyGrandma")
    cursor = d.find_element(By.ID, "buyCursor")

    # MONEY AND COST VARIABLES
    total_cookies = int(d.find_element(By.ID, "money").text.replace(",", ""))
    cost_cursor = int(d.find_element(By.ID, "buyCursor").find_element(By.TAG_NAME, "b").text.strip("Cursor - ").replace(",", ""))
    cost_grandma = int(d.find_element(By.ID, "buyGrandma").find_element(By.TAG_NAME, "b").text.strip("Grandma - ").replace(",", ""))
    cost_factory = int(d.find_element(By.ID, "buyFactory").find_element(By.TAG_NAME, "b").text.strip("Factory - ").replace(",", ""))
    cost_mine = int(d.find_element(By.ID, "buyMine").find_element(By.TAG_NAME, "b").text.strip("Mine - ").replace(",", ""))
    cost_shipment = int(d.find_element(By.ID, "buyShipment").find_element(By.TAG_NAME, "b").text.strip("Shipment - ").replace(",", ""))
    cost_lab = int(d.find_element(By.ID, "buyAlchemy lab").find_element(By.TAG_NAME, "b").text.strip("Alchemy lab - ").replace(",", ""))
    cost_portal = int(d.find_element(By.ID, "buyPortal").find_element(By.TAG_NAME, "b").text.strip("Portal - ").replace(",", ""))
    cost_time_machine = int(d.find_element(By.ID, "buyTime machine").find_element(By.TAG_NAME, "b").text.strip("Time machine - ").replace(",", ""))

    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:
        if total_cookies > cost_time_machine:
            time_machine.click()
        elif total_cookies > cost_portal:
            portal.click()
        elif total_cookies > cost_lab:
            lab.click()
        elif total_cookies > cost_shipment:
            shipment.click()
        elif total_cookies > cost_mine:
            mine.click()
        elif total_cookies > cost_factory:
            factory.click()
        elif total_cookies > cost_grandma:
            grandma.click()
        elif total_cookies > cost_cursor:
            cursor.click()

