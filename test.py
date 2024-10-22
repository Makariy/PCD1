import time

from config import BRANDS_TO_PARSE
from driver import create_webdriver, create_webdriver_options
from driver.interactor import Interactor
from driver.paginator import Paginator
from driver import Driver


def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=True)
    )

    # create Interactor
    interactor = Interactor(driver, "https://pcpartpicker.com/products/video-card/")

    # get into the URL
    driver.get("https://pcpartpicker.com/products/video-card/")

    for vendor in BRANDS_TO_PARSE:
        interactor.select_vendor(vendor)
        print(driver.current_url)
        time.sleep(3)


if __name__ == "__main__":
    main()
