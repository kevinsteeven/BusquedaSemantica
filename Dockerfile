#usar una imagen base de Python
FROM python:3.11-slim

#Instalar librerias
RUN pip install -U sentence-transformers pandas

#Establecer el directorio de trabajo en /app
WORKDIR /app

#Copiar el archivo de python y el archivo de texto a la imagen
COPY src ./src/

#Crear volumen
VOLUME ./app/src

#Comando que se se ejecuta al iniciar el contenedor
CMD ["python","src/main_students.py"]