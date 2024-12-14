
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
