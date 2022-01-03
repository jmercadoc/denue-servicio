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
![Screenshot 2022-01-02 at 20-33-27 Flasgger](https://user-images.githubusercontent.com/44456304/147899923-cba01a15-5609-4554-b8af-9f00c7970abd.png)

### Ejemplos de consultas
- Mostrar los negocios del estado de Zacatecas 
[127.0.0.1:5000/estados/zacatecas/negocios](http://127.0.0.1:5000/api/v1/estados/zacatecas/negocios)
![Screenshot 2022-01-02 at 20-34-13 http 127 0 0 1 5000 api v1 estados zacatecas negocios](https://user-images.githubusercontent.com/44456304/147899940-b037dd11-660d-4f45-a7b8-cb43a260ea5c.png)

- Mostrar los restaurantes del estado de Zacatecas 
[127.0.0.1:5000/estados/zacatecas/negocios/restaurantes](http://127.0.0.1:5000/api/v1/estados/zacatecas/negocios/restaurantes)
![Screenshot 2022-01-02 at 20-34-33 http 127 0 0 1 5000 api v1 estados zacatecas negocios restaurantes](https://user-images.githubusercontent.com/44456304/147899951-b9a1e815-7961-488c-9898-465d7b6e4ecc.png)

- Mostrar los restaurantes del estado de Zacatecas en los municipios de Fresnillo y Guadalupe 
[127.0.0.1:5000/estados/zacatecas/negocios/restaurantes?ubicacion=fresnillo&ubicacion=guadalupe](http://127.0.0.1:5000/api/v1/estados/zacatecas/negocios/restaurantes?ubicacion=fresnillo&ubicacion=guadalupe)
![Screenshot 2022-01-02 at 20-34-54 http 127 0 0 1 5000 api v1 estados zacatecas negocios restaurantes ubicacion=fresnillo ub](https://user-images.githubusercontent.com/44456304/147899963-3911e9aa-855a-4da2-9645-e7ab019d939c.png)


