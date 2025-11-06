from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    time.sleep(1)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    time.sleep(1)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(1)
    assert "inventory.html" in driver.current_url
    
