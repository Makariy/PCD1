import time

from config import BRANDS_TO_PARSE
from driver import create_webdriver, create_webdriver_options
from driver.interactor import Interactor
from driver.paginator import Paginator
from driver import Driver


def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=False)
    )

    # get into the URL
    driver.get("https://pcpartpicker.com/products/video-card/")

    interactor = Interactor(driver, "https://pcpartpicker.com/products/video-card/")
    paginator = Paginator(driver)
    time.sleep(3)
    for vendor in BRANDS_TO_PARSE:
        interactor.select_vendor(vendor)
        while paginator.has_next_page():
            paginator.navigate_to_next_page()

    time.sleep(10)




if __name__ == "__main__":
    main()
