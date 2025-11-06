from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    driver.find_element("id", "react-burger-menu-btn").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    driver.find_element("id", "logout_sidebar_link").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("saucedemo.com")
    )

    assert "saucedemo.com" in driver.current_url