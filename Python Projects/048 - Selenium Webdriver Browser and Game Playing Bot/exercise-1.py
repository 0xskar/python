from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.amazon.ca/Bitdefender-Total-Security-Subscription-Activation/dp/B07XPGZ7DF?ref_=Oct_d_omwf_d_3318461_0&pd_rd_w=OBAIK&content-id=amzn1.sym.1dd15c99-95b0-4ea5-8749-96ac70aa66a9&pf_rd_p=1dd15c99-95b0-4ea5-8749-96ac70aa66a9&pf_rd_r=99A5Q5SXX10YNQ9NTQYG&pd_rd_wg=Txe61&pd_rd_r=6ad4168f-f479-4f5d-b902-aa00d82adcfe&pd_rd_i=B07XPGZ7DF")

prices = driver.find_element(By.CLASS_NAME, "a-price")
print(prices.text)

driver.close()
