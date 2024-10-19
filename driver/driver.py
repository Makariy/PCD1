from selenium.webdriver import Firefox
# from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions 
# from selenium.webdriver.chrome.options import Options as ChromeOptions 

Driver = Firefox
Options = FirefoxOptions


def create_webdriver_options(
        is_headless=True
) -> Options:
    options = Options()
    if is_headless:
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options


def create_webdriver(
        options: Options | None = None,
) -> Driver:
    if options is None:
        options = create_webdriver_options()
    return Driver(options=options)


