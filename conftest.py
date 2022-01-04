import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.pages.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logging.basicConfig(filename="grocery_store.log", level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/online-grocery-store/",
        help="Grocery store url",
    )


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--url")
    s = Service(ChromeDriverManager().install())

    # chrome_options.headless = True
    # chrome_options.add_argument("--kiosk")
    # driver = webdriver.Chrome(service=s)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(options=chrome_options)

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # str = ChromeDriverManager().install()
    # print(str)
    driver = webdriver.Chrome(service=s, options=chrome_options)

    driver.maximize_window()
    logger.info(f"Start app on {url}.")
    app = Application(driver, url)
    yield app
    app.quit()
