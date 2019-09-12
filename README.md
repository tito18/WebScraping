# WebScraping

Para que corra deben instalar primero cada libreria.
A continuacion les dejo el comando nama para que copien y peguen:
#pip install requests beautifulsoup html5lib urllib string

La guia que vi para armar esto es: https://likegeeks.com/es/web-scraping-beautiful-soup-y-selenium/#Esperar-a-que-la-llamada-Ajax-sea-completada-usando-PhantomJS 

La documentacion de BeatifulSoup4 es: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#extract  

- imagenString convierte el contenido de la variable "LinkRAW" en un string.
- ima dividimos la cadena en dos variables distintas donde la primera se encuentra todo lo que esta antes de los caracteres "src=" y en la otra variable se encuentra lo que esta despues de estos caracteres.
- ima2 realizamos los mismo que con "ima" solo que los caracteres de evaluo vienen a ser el salto de linea "\n".
- imagenURL realizamos lo mismo que con los "ima" y "ima2" solo que en este el caracter son una doble comilla (").

- linkString convierte el contenido de la variable "LinkRAW" en un string.
- linkString1 dividimos la cadena en dos variables distintas donde la primera se encuentra todo lo que esta antes de los caracteres "href=" y en la otra variable se encuentra lo que esta despues de estos caracteres.
- linkString2 realizamos los mismo que con "linkString1" solo que los caracteres de evaluo vienen a ser el salto de linea "\n".
- link realizamos lo mismo que con los "linkString1" y "linkString2" solo que en este el caracter son una doble comilla (").
