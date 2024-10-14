
# Como testear vuestro codigo

Para testear el codigo, abres test.py y modificas desde los ... en la funcion main.
Por ejemplo para testear el driver.paginator, modificas main de la siguiente manera:
```python 
def main():
    driver = create_webdriver(
        options=create_webdriver_options(is_headless=False)
    )
    # Suponemos que ya estamos en la pagina del vendedor
    driver.get("https://www.pccomponentes.com/tarjetas-graficas/asus")

    # Inicializamos el Paginator
    paginator = Paginator(driver)

    # Vemos si hay siguiente pagina?
    print(f"{paginator.has_next_page()}")
    
    # Vemos como es la pagina 
    time.sleep(5)
    # Vemos como pulsamos el boton de la siguiente pagina
    paginator.navigate_to_next_page()
    
    # Vemos como ha pulsado el boton de next page
    time.sleep(10)
```

