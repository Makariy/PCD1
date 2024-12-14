
## Instalacion
Las dependencias del proyecto estan ubicadas en el archivo `plots_requirements.txt`. <br/>
Principalmente se utilizan las siguientes librerias:
- Plotly (5.24.1)
- Pandas (2.2.3)

Para instalar las dependencias del proyecto vamos a crear un virtual environment usando venv de Python. 
```bash
python3 -m venv venv 
. ./venv/bin/activate
python3 -m pip install -r plots_requirements.txt
```

---
### Ejecucion de los graficos
Los scripts `.py` que se usan para crear los graficos de la presentacion estan ubicados en el directorio `./plots`
de los cuales, se usan los siguientes:
- `correlation_matrix.py`
- `boxplot_core_clock_to_price.py`
- `brands_cmparison_with_heuristic.py`
- `brands_cmparison_with_user_score.py`
- `card_by_budget.py`


Para la ejecucion de estos scripts, se tiene que ubicarse en el directorio plots y 
ejecutar el script correspondiente al grafico que se quiere ejecutar. Por ejemplo ejecutaremos el archivo 
`correlation_matrix.py`:
```bash
. ./venv/bin/activate
cd plots 
python3 correlation_matrix.py 
```
Y se mostrara el grafico correspondiente

---
## Explicacion de los archivos
Los graficos usados en la presentacion se generan con los siguientes scripts:
- `correlation_matrix.py`
Crea la matriz de correlacion para las columnas `price, memory, core_clock, core_boost_clock`
- `boxplot_core_clock_to_price.py` 
Crea el diagrama de caja construida a partir de la expresion `core_boost_clock/price` para las tarjetas graficas RTX 
de la serie 40
- `brands_cmparison_with_heuristic.py` Crea un diagrama de barras comparando por una heuristica las marcas 
- `brands_cmparison_with_user_score.py` Crea un diagrama de barras comparando por `user_score` las marcas
- `card_by_budget.py` Crea un diagrama de barras de las mejores tarjetas graficas en orden descendiente de la heuristica
debajo del precio establecido

Ademas de los archivos que crean los graficos, tambien se han usado unos archivos de utilidad:
- `dataframe.py` Crea la variable `df` de tipo `pandas.DataFrame` que une todos los datos recolectados a partir 
de Web Scrapping y ademas define la variable `columns` que contiene todas las columnas de `df`
- `utils.py` Define las funciones de utilidad que se han usado en la generacion de las graficas como la heuristica

