import time
from driver import create_webdriver, create_webdriver_options
from driver.interactor import Interactor
from driver.paginator import Paginator
from driver import Driver


def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=False)
    )
    driver.get("https://pcpartpicker.com/products/video-card/")

    time.sleep(2)
    paginator = Paginator(driver)
    time.sleep(3)
    # paginator.accept_cookies()
    for i in range(3):
        print(f"{paginator.has_next_page()=}")
        time.sleep(2)
        # paginator.navigate_to_next_page()

    time.sleep(100)


if __name__ == "__main__":
    main()
