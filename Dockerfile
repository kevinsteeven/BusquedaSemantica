#usar una imagen base de Python
FROM python:3.11-slim

#Instalar librerias
RUN pip install -U sentence-transformers pandas

#Establecer el directorio de trabajo en /app
WORKDIR /app

#Copiar el archivo de python y el archivo de texto a la imagen
COPY semantic_search/ ./semantic_search/

#Crear volumen
VOLUME ./app/semantic_search

#Comando que se se ejecuta al iniciar el contenedor
CMD ["python","semantic_search/main_students.py"]