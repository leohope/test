import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    chrome_options = Options()

    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()
    shutil.rmtree(user_data_dir)

def test_login(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"
