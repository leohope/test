import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Remote(command_executor="http://selenium-chrome:4444/wd/hub", options=chrome_options)

    driver.implicitly_wait(10)
    return driver


def test_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"
    driver.quit()
