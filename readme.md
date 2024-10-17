
# Buscador de películas semántico

Con este programa podras buscar peliculas desde una base de datos de IMDB. En este programa se veran implementados los principios SOLID (Los principios S: Single Responsability y D:Dependency inversion) y el patron de diseño Facade

## ¿Como usar el programa?

- Tener en cuenta que es necesario tener instalado Docker, desde la diguiente URL se puede descargar: https://www.docker.com/
- Clonar este repositorio.
```
git clone https://github.com/kevinsteeven/BusquedaSemantica
```
- Crear una imagen de docker a partor del dockerfile presente en este repositorio, esto se puede realizar usando el comando de consola 'docker build -t'(Más información sobre el comando en:https://docs.docker.com/reference/cli/docker/buildx/build/).
```
docker build -t <nombre_imagen> .
```
- Luego se debe crear un contenedor a partir del volumen de la imagen creada, esto se puede realizar usando el comando de consola 'docker run -it -v'. Es importante tener en cuenta el parametro '-it' ya que va a permitir la interaccion con la consola(Más información sobre el comando en:https://docs.docker.com/reference/cli/docker/container/run/).

Comando para Windows:
```
docker run -it -v "%cd%"/semantic_search:/app/semantic_search <nombre_imagen>
```
Comando para Linux:
```
docker run -it -v "$(pwd)/semantic_search:/app/semantic_search" <nombre_imagen>
```
- Ingresar en la consola la frase a partir de la cual se quiere hacer la busqueda de la pelicula y dar enter, si se desea detener el programa dar enter sin ingresar nada en el campo de busqueda de la consola.

En el proyecto se encuentra adicionalmente un archivo requirements.txt, en este archivo se encuentran librerias necesarias para ejecutar pruebas del proyecto, mas no para la ejecucion del proyecto en si

### ¿Como realizar test?
Para realizar los test unitarios presentes en el proyecto se pueden seguir los siguientes pasos(Los dos primeros pasos consisten en la creación y activación de un entorno virtual, lo cual no es obligatorio pero si es recomendable para evitar conflictos con otros complementos en la maquina donde se realizara la ejecución):

-Crear entorno virtual
```
python -m venv venv
```
-Activar entorno virtual
```
.\venv\Scripts\activate
```

-Realizar instalacion de las librerias necesarias
```
pip install -r requirements.txt
```

-Ejecutar test con pytest
```
python -m unittest  discover -v tests/
```