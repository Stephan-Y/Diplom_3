import pytest
from data.data import TestData
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser! Please choose 'chrome' or 'firefox'.")

    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    driver.get(TestData.URL)
    yield driver
    driver.quit()
