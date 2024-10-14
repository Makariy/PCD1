from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


Driver = Firefox

def create_webdriver_options(
        is_headless=True
) -> Options:
    options = Options()
    options.headless = is_headless
    if is_headless:
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options


def create_webdriver(
        options: Options = None,
) -> Firefox:
    if options is None:
        options = create_webdriver_options()
    return Firefox(options=options)


