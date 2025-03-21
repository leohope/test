import pytest
from selenium import webdriver

SELENIUM_GRID_URL = "http://selenium-hub:4444/wd/hub"


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")

    options = None
    if "chrome" in browser_name:
        options = webdriver.ChromeOptions()
    elif "firefox" in browser_name:
        options = webdriver.FirefoxOptions()

    if "remote" in browser_name:
        driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)
    else:
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options) if browser_name == "chrome" else webdriver.Firefox(options=options)

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome, firefox, remote_chrome, remote_firefox")
