# Consulta Negocios

Crear un servicio que proporcione la información de los negocios por localidades (Municipio/Delegación) del  [INEGI](https://www.inegi.org.mx/servicios/api_denue.html).

# Instrucciones
## Prerrequisitos
- Verificar la versión de python
```sh
$ python --version
o
$ python3 --version
```
- El API fue desarrollada utilizando Python 3.9.7 
- En caso de no tener instalada la versión de Python seguir los indicados [aquí](https://www.python.org/downloads/)
- Crear un entorno virtual
```sh
$ python -m venv venv
```
- Correr el entorno virtual
### Linux
```sh
$ cd "venv"
$ source bin/activate
```
### Windows
```sh
> .\venv\Scripts\activate
```

- Instalar requerimientos
```sh
$ pip install -r requirements.txt
```

- Verificar la siguiente información en el archivo .env
```
DENUE_URL='https://www.inegi.org.mx/app/api/denue'
DENUE_TOKEN=61305901-a81f-46d9-81a2-5497fde81fa5
WSCATGEO_URL='https://gaia.inegi.org.mx/wscatgeo'
DOCS_URL='http://127.0.0.1:5000'
```
Nota: El archivo .env fue subido a GitHub de manera intencional para exponer el Token necesario para consumir la información del INEGI, esto es una mala práctica pero se realiza para facilitar la demostración del API, el token fue generado con un correo temporal [aqui](https://10minutemail.net)

- Correr el servidor
```sh
$ python main.py
```

- Para correr los test
```sh
$ pytest
```
Nota: El servicio del INEGI podría bloquear temporalmente las peticiones si se excede el límite establecido.

El servidor se ejecutará en la dirección [127.0.0.1:5000/](http://127.0.0.1:5000/).
La raíz del proyecto / mostrará la documentación de swagger en donde se explican los parámetros necesarios y forma de utilizar el API

### Ejemplos de consultas
- Mostrar los negocios del estado de Zacatecas 
[127.0.0.1:5000/estados/zacatecas/negocios](http://127.0.0.1:5000/api/v1/estados/zacatecas/negocios)

- Mostrar los restaurantes del estado de Zacatecas 
[127.0.0.1:5000/estados/zacatecas/negocios/restaurantes](http://127.0.0.1:5000/api/v1/estados/zacatecas/negocios/restaurantes)

- Mostrar los restaurantes del estado de Zacatecas en los municipios de Fresnillo y Guadalupe 
[127.0.0.1:5000/estados/zacatecas/negocios/restaurantes?ubicacion=fresnillo&ubicacion=guadalupe](http://127.0.0.1:5000/api/v1/estados/zacatecas/negocios/restaurantes?ubicacion=fresnillo&ubicacion=guadalupe)


