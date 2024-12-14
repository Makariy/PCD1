Grupo 07: Joaquin Negrete Saab, Makar Isaev, Oliver Arnaldo Anderson LLorens y Pablo Suárez Iglesias

Temática: Para la temática se ha escogido hacer scraping de diferentes tarjetas gráficas y sus diferentes datos asociandos.

Source: https://pcpartpicker.com/

Obstáculos encontrados: 
1. La idea inicial era hacer scraping sobre la web de Pccomponentes (https://www.pccomponentes.com/). Sin embargo, encontramos que al navegar por varias pestañas terminaba por mostrar, inevitablemente, un captcha de cloudfare que no pudimos evitar, ni siquiera enviando headers, esperando tiempos aleatorios entre clicks o usando metodos de <<stealth>>. 
2. Otro inconveniente fue que uno de los integrantes del grupo fue baneado de la página web al intentar hacer scraping, sin embargo nos percatamos de que puede seguir entrando y haciendo scraping con total normalidad al usar la vpn de la universidad u otra cualquiera. Seguimos sin ser conscientes de cual fue la razón de ser baneado, pues ningún otro integrante lo fue.
Observaciones:
1. La idea inicial era, al entrar a la lista de tarjetas gráficas, entrar a cada una de ellas para recoger información de ella y retornar para entrar a otra. Sin embargo, esto conlleva varios inconvenientes, entre ellos un aumento enorme del tiempo de ejecución y un aumento en la posibilidad de  ser detectado y rechazado por la enorme cantidad de peticiones del bot. Además vimos que la información más preciada y aquella que teníamos pensado recabar se encontraba listada junto al nombre de la tarjeta gráfica, por lo que no había necesidad de entrar al propio link de cada  tarjeta individual. Aun tras esto el programa era bastante lento, conseguimos agilizarlo mediante el uso de scraping estático con Beautifulsoup. De esta manera el scraping es casi inmediato para cada página.

Información recabada:
	Marcas: Asus, Gigabyte, MSI, XFX, Zotac
	Datos: name, parent_brand, price, memory, core_clock, core_boost_clock, length, user_score, user_ratings_count, chipset

Visualización:

Archivos: 
	Todos los scripts usados en el tratamiento y visualización de datos se han guardado en la carpeta <<plot>>, en forma de archivos .py.
utils.py contiene una serie de funciones útiles a la hora de tratar los datos, como una función para estandarizar o calcular una heurística propia.
dataframe.py se encarga de crear dataframe que unifica los csv's a usar (Asus.csv, Gigabyte.csv y MSI.csv)
El resto de los archivos se encarga de tratar los datos y crear gráficas, una gráfica para cada archivo. Estos se pueden ejecutar de manera independiente.
Aunque el orden podría ser cualquiera, se recomienda seguir el siguiente: 1. correlation_matrix.py, 2. boxplot_core_clock_to_price.py, 3.
brands_comparison_with_heuristic.py, 4. brands_comparison_with_user_score.py, 5. card_by_budget.py
	
Dependencias:
	Las principales librerias usadas en esta segunda parte son pandas (2.2.3), para la generación y tratamiento de lod datos, y plotly (5.24.1), para la creación de los gráficos. Se puede ver más en detalle todas las dependencias en el archivo requirements.txt. Para instalar todas estas basta con escribir pip install -r requirements.txt

