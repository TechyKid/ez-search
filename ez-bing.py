from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

a = 1

while a==1: 
    search = input("What would you like to search you lazy person: ")
    time.sleep(0.5)
    driver = webdriver.Chrome()
    driver.get("https://bing.com")
    driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').click()
    driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').send_keys(search)
    driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').send_keys(Keys.RETURN)
