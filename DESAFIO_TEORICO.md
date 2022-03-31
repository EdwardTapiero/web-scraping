# Desafio teórico

## Procesos

En el momento en que tenga que ejecutar secuencialmente usaría procesos ya que hasta que no finalice el primero no continuará el segundo y/o los demás, por ejemplo obtener datos de una base de datos y luego que realice ese proceso se parsea algun campo que sea necesario o mapearlo a la respuesta esperada, no podríamos hacer una acción sin haber finalizado la siguiente

## Hilos
Con el fin de ejecutar dos instancias al mismo tiempo, llamado concurrencia, por ejemplo podría aplicarlo haciendo un cronometro y otra tarea en paralelo a la vez va a realizar otra acción, otro caso sería si tenemos un supermecado y solo un cajero y dos clientes, si usaramos hilos, podríamos tener por ejemplo 2 cajeros atentiendo a cada cliente y de esta manera reducir el tiempo

## Corrutinas

En este caso tras ejecutarse una función puede quedarse pausada y guardar el valor de variables hasta que se vuelva a reanudar, por ejemplo almacenar información que se accede multiples veces en un for


## Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos inforación en una API HTTP. ¿Cómo lo harías? 
La mejor forma a mi punto de vista sería dividir por partes o páginas la información, indicandolo a traves de un request param el tamaño de elementos a traer 