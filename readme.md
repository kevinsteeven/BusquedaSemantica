
# Buscador de películas semántico

Con este programa podras buscar peliculas desde una base de datos de IMDB.

## ¿Como usar el programa?

- Tener en cuenta que es necesario tener instalado Docker, desde la diguiente URL se puede descargar: https://www.docker.com/
- Clonar este repositorio.
- Crear una imagen de docker a partor del dockerfile presente en este repositorio, esto se puede realizar usando el comando de consola 'docker build -t'.
- Luego se debe crear un contenedor a partir del volumen de la imagen creada, esto se puede realizar usando el comando de consola 'docker run -it -v'. Es importante tener en cuenta el parametro '-it' ya que va a permitir la interaccion con la consola
- Ingresar en la consola la frase a partir de la cual se quiere hacer la busqueda de la pelicula y dar enter, si se desea deteenr el programa dar enter sin ingresar nada en el campo de busqueda de la consola.