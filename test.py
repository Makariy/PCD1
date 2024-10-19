import time
from driver import create_webdriver, create_webdriver_options
from driver.interactor import Interactor
from driver.paginator import Paginator
from driver import Driver


def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=False)
    )
    driver.get("https://www.pccomponentes.com/tarjetas-graficas/asus")

    paginator = Paginator(driver)
    time.sleep(2)
    paginator.accept_cookies()
    for i in range(10):
        print(f"{paginator.has_next_page()=}")
        time.sleep(1)
        paginator.navigate_to_next_page()
        time.sleep(1)


if __name__ == "__main__":
    main()
