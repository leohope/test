import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, expected_message", [
    ("test_user", "secret123", "Welcome, test_user"),
    ("wrong_user", "wrong_pass", "Invalid username or password")
])
def test_login(driver, username, password, expected_message):
    driver.get("https://example.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    message = driver.find_element(By.ID, "message").text
    assert expected_message in message