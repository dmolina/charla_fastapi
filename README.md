# Charla sobre FastAPI

 Charla en Español sobre [FastAPI](https://fastapi.tiangolo.com/es/) (Talk in
 Spanish about [FastAPI](https://fastapi.tiangolo.com/es/))

## Directorios

El directorio actual contiene las transparencias en formato reveal.js. 

El directorio */demo* contiene la demo mencionada en las transparencias.

## Instalación

Requiere python versión 3. Las dependencias de los paquetes de python se pueden
instalar con:

```sh
$ pip install poetry # Para gestionar dependencias
$ cd demo # Ir al directorio de los recursos webs
$ poetry install # Instala las dependencias necesarias
```

## Ejecutación

Para lanzar los servicios REST es necesario ejecutar:

```sh
$ cd demo
$ hypercorn <name>:app --reload
```

Donde <name> puede ser:

- **test:** ejemplos usados en la presentación.

- **seriesfliz:** Ejemplo de demo en modo estático (sin Base de Datos).

La opción *reload* permite editar el fichero y se se aplica directamente.

La anterior es la opción recomendada, por la opción *reload*. De todos modos, 
para ejectarlo también se puede usar:

```sh
$ python server.py
```

La web de ejemplo es totalmente estática, solo requiere JavaScript. Para
ejecutarlo se puede usar el siguiente comando en el directorio del proyecto:

```sh
$ python -m http.server 8100 >/dev/null
```

Eso permitirá acceder a la página web de demo con [http://localhost:8100/page.html](http://localhost:8100/page.html)
