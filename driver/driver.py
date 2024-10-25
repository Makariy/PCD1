# from selenium.webdriver import Firefox
from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service

Driver = Chrome
Options = ChromeOptions


def create_webdriver_options(
        is_headless=True
) -> Options:
    options = Options()
    if is_headless:
        options.add_argument("--headless")

    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    return options


def create_webdriver(
        options: Options | None = None,
) -> Driver:
    if options is None:
        options = create_webdriver_options()
    driver = Driver(
        options=options,
    )
    return driver
