from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

a = 1

while a==1:
    search = input("What would you like to search you lazy person: ")
    time.sleep(0.5)
    driver = webdriver.Chrome()

    driver.get("https://google.com")
    sbox = driver.find_element(By.NAME, "q")
    sbox.send_keys(search)
    sbox.send_keys(Keys.RETURN)
