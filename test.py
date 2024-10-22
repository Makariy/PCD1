import time
from driver import create_webdriver, create_webdriver_options
from driver.interactor import Interactor
from driver.paginator import Paginator
from driver import Driver


def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=False)
    )

    # create Interactor
    interactor = Interactor(driver, "https://pcpartpicker.com/products/cpu")

    # get into the URL
    driver.get("https://pcpartpicker.com/products/cpu")
    driver.maximize_window()
    time.sleep(5)

    # accept cookies
    interactor.accept_cookies()
    time.sleep(5)

    # change to AMD cpu's
    interactor.select_vendor("AMD")
    time.sleep(5)


if __name__ == "__main__":
    main()
