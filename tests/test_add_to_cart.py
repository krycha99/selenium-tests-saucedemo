from selenium import webdriver

def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    driver.find_element("xpath", "//button[contains(text(),'Add to cart')]").click()
    driver.find_element("class name", "shopping_cart_link").click()

    assert "Your Cart" in driver.page_source