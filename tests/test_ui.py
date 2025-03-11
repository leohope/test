import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"