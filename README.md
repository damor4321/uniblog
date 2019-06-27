UniBlog - Docker
================

Se usa Docker + Django + DRF

La aplicacion está rota por falta de tiempo.

En "api" están los componentes de la API de Blog

La parte consumidora de la api está en "blog" y esta sin hacer.

### Prerequisito

* Tener instalado **Docker**.


**_Paso 1: Crear Imagen en Docker_**

Se crea la imagen de Docker para el proyecto. La imagen va a contener la instalación de los requerimientos establecidos en el fichero `requirements.txt`.

El fichero `requirements.txt` contiene los requisitos básicos para el inicio y despliegue de una aplicación con Django, si necesita adicionarle nuevos elementos este es un buen momento.

```
docker build -t uniblog:1.0 .
```

Siempre que modifique los elementos dentro del fichero `requirements.txt` tiene que repetir este paso.


**_Paso 2: Iniciar el Docker_**
Se ejectua el siguiente comando. En el navegador se puede revisar la aplicación en la siguiente dirección `http://<ip-máquina:8000>`. El puerto de salida puede ser configurado en el fichero `docker-compose.yml`.
```
docker-compose up
```

**_Paso 3: Parar el Docker_**
Se detiene el sistema de ser necesario para continuar con las configuraciones.
```
Ctrl-C
```

