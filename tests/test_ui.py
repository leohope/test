from selenium.webdriver.common.by import By


def test_login_success(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    browser.find_element(By.ID, "username").send_keys("student")
    browser.find_element(By.ID, "password").send_keys("Password123")
    browser.find_element(By.ID, "submit").click()

    success_message = browser.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"


def test_login_fail(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    browser.find_element(By.ID, "username").send_keys("incorrectUser")
    browser.find_element(By.ID, "password").send_keys("Password123")
    browser.find_element(By.ID, "submit").click()

    invalid_message = browser.find_element(By.ID, "error").text
    assert invalid_message == "Your username is invalid!"
