#importing required packages - need to pip3 install selenium first !
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
#adding options on Chrome
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
#location by name
driver=webdriver.Chrome(options=chromeOptions)
driver.get("https://pluralsight.com/")

ele=driver.find_element_by_name("q")
time.sleep(1)
ele.clear()
ele.send_keys("Pratheerth Padman")
ele.send_keys(Keys.RETURN)
driver.quit