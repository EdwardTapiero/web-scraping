# Web scraping

Busca los productos de mercado libre, sección celulares-smartphones, de la páginación especificada , guarda la información en una base de datos MySQL y realiza el conteo de la cantidad de productos que hay por marca indicada

## Tecnologías y librerias usadas

-   Flask
-   Jsonify
-   Requests
-   MySQL
-   BeautifulSoup
-   lxml

## ¿Cómo ejecutar?

Clona el repositorio o descarga el repositorio en formato ZIP

**web-scraping**

  1. Ingresa a la ruta `cd web-scraping` desde la consola
  2. Allí se encontrará el script de la base de datos con el fin de crear la tabla, el nombre del archivo es `script_db.sql` encontrado en la raiz del proyecto
  3. Ejecuta el comando `pip install -r ./requirements.txt`.
  4. Ejecuta el comando `python app.py`.
  5. Se ejecutará por defecto en [localhost:5002]().

##### Notas
- _La versión recomendable de python es = 3.10_
- _Si hay mas de una versión intalada de python reemplazar comando pip por pip3 y python por python3_

## ¿Cómo usar?

Se crea un API con el fin de obtener la informacón a partir de REST

 **Características del API**

|Característica|Descripción|
| :-: | :-: |
|**Método de transferencia**|REST|
|**Sintaxis**|Request Params|
|**Método HTTP**|GET|
|**Path**|/api/v1/mercado_libre/consulta_marca|

**Request param**

|Nombre parámetro|Descripción|Valor por defecto|
| :-: | :-: | :-: |
|reset|Si su valor es true realizará una nueva consulta a la pagina de mercado libre para ver los datos actuales y eliminará los datos anteriores, si su valor es false hará el conteo con la ultima información guardada en base de datos|false|
|pagination|Especifica hasta que paginación horizantal se desea llegar en la consulta|5|
|brand|Indica que marca de celular se desea hacer el conteo|Samsung|

**Campos de response**
|Campo|Descripción|
| :-: | :-: |
|Marca|Marca de celular buscado para hacer el conteo|
|Paginas buscadas|Cantidad de paginación buscada horizontalmente|
|Registros encontrados por marca|Cantidad de celulares encontrados por la marca indicada|
|Nueva busqueda|Campo booleano que indica si fue una nueva consulta o se tomo los datos existentes en base de datos, hace relación con el campo reset del request param|

**Ejemplo Request**
```sh
http://localhost:5002/api/v1/mercado_libre/consulta_marca?reset=true&pagination=1&brand=Xiaomi
```
**Ejemplo Response**

```json
{
  "Datos": {
    "Marca": "Samsung", 
    "Nueva busqueda": false, 
    "Paginas buscadas": 5, 
    "Registros encontrados por marca": 66
  }
}
```
> Se adjunta postman