import pytest
import configparser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

config = configparser.ConfigParser()
config.read("./settings.conf")


# @pytest.fixture(params=["chrome", "firefox"])
# def setup(request):
#     browser_name = request.param
#     if browser_name == "chrome":
#         driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")

# yield driver
# driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # service_obj = Service(config['cm']['CHROME_DRIVER_LOCATION'])
        # driver = webdriver.Chrome(service=service_obj)
        driver = webdriver.Chrome(options=options)


    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        service_obj = Service(executable_path=config['cm']['MS_EDGE_DRIVER_LOCATION'])
        driver = webdriver.Edge(service=service_obj, options=options)

    elif browser_name == "headless":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("window-size=1920x1080")
        driver = webdriver.Chrome(options=options)

    driver.get(config['cm']['TEST_URL'])
    driver.maximize_window()
    request.cls.driver = driver
    yield

    driver.close()
    driver.quit()
