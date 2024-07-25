import pytest
import os
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Set up Selenium WebDriver and quit it after use
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="session",autouse=True)
def environment():
    env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_env"))
    with open(env_file, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            sep = line.find("=")
            if sep > 0:
                key = line[:sep]
                value = line[sep + 1:].strip()
                os.environ[key] = value
    if not os.path.exists(os.environ['SCREENSHOT_PATH']):
        os.makedirs(os.environ['SCREENSHOT_PATH'])