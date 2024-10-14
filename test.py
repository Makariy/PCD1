import time
from driver import create_webdriver, create_webdriver_options
from driver.paginator import Paginator


def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=False)
    )
    ...


if __name__ == "__main__":
    main()
