from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user=''
pw=''
driver=webdriver.Firefox()
driver.get('https://www.facebook.com')
element=find_element_by_id('email')
element.send_keys(user)
element=driver.find_element_by_id('pass')
element.send_keys(pw)
element.send_keys(Keys.RETURN)
element.close()