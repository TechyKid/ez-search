from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
search = input("What would you like to search you lazy person: ")

driver = webdriver.Chrome()

driver.get("https://google.com")
time.sleep(1)
sbox = driver.find_element(By.NAME, "q")
sbox.send_keys(search)
sbox.send_keys(Keys.RETURN)
