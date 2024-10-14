
# Practica 1 de programacion para ciencia de datos

Copiais el proyecto con 
```shell
cd ~/vuestra_carpeta/
git clone https://github.com/Makariy/PCD1.git
cd PCD1
pwd
```
Abris el proyecto localizado en el directorio que dice ``pwd`` en PyCharm y haceis lo vuestro

Una vez terminado
```shell
git add .
git commit -m "<Cambio hecho> - <Tu nombre>"
git push 
```

Lo que hace es entrar en https://www.pccomponentes.com/tarjetas-graficas. 
Despues driver.interactor pulsa el boton 'ver mas' que esta situado a la izquierda en filtros y elige la marca. 

El driver.parser parsea todas las tarjetas graficas que hay y las devuelve como una lista.

El driver.paginator si hay una siguiente pagina, pulsa el boton para pasar a la siguiente. 

Cuando hemos obtenido todas las tarjetas graficas para cada marca, las guardamos usando serializer.

