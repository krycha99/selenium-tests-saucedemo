from selenium import webdriver

def test_remove_button(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    driver.find_element("class name", "inventory_item_name ").click()
    add_button = driver.find_element("xpath", "//button[contains(text(),'Add to cart')]")
    add_button.click()
    driver.find_element("xpath", "//button[contains(text(),'Remove')]").click()

    assert "Add to cart" in driver.page_source