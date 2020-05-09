# Tarea 1

El presente proyecto realiza web scrapping con paginación al sitio https://en.wikipedia.org/wiki/Wikipedia:Featured_articles.

# 1. Prerequisitos

1. Crear la carpeta **Data** en el disco local C:. Si en caso se trabaja en Linux o si se desea utilizar otro directorio para guardar el JSON de salida, dirigirse al archivo ubicado en **./tarea1wiki/spiders/articleswiki.py en la línea 14** y cambiar el directorio de salida.

2. Instalar Python 3.7.6 y scrapy. Nota: se puede crear un ambiente virtual de Python para ejecutar el proyecto, siempre que cuente con los módulos mencionados. Si se utiliza ambiente virtual, se asume que el usuario ya se encontrará dentro de este previo a ejecutar las instrucciones mencionadas en al sección 2.

# 2. Instrucciones para ejecutar el proyecto

1. Mediante una terminal, ingresar a la carpeta donde se encuentra el proyecto y correr el comando **scrapy crawl articleswiki**.

2. Verificar que se haya generado el archivo JSON en el directorio configurado.

# 3. Nota

En el presente repositorio se encuentra el archivo **featured_article-2020-05-09T04-16-03.json**, el cual es una salida de ejemplo generada mediante la ejecución de las instrucciones de la seccion 2.
