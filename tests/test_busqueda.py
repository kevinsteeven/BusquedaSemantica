import unittest
import pandas as pd
from sentence_transformers import SentenceTransformer
import os.path as path#libreria importada para validar excepcion de si no se encuentra el archivo. documentacion: https://docs.python.org/es/3.10/library/os.html
from src.main_students import validar_fin,aumentar_contexto,compute_similarity,BusquedaDB
class testBusqueda(unittest.TestCase):
    def test_fin(self):
        '''Prueba la funcion que valida si se desea detener el programa'''
        prueba=validar_fin("")
        self.assertTrue(prueba)
        prueba=validar_fin("Heat")
        self.assertFalse(prueba)
    def test_contexto(self):
        '''Prueba la funcion que genera los embeddings a partir de varias columnas del dataframe'''
        df = pd.read_csv('././src/data/IMDB top 1000.csv')
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        prueba=aumentar_contexto(df,model)
        self.assertEqual(len(prueba),df.shape[0])#Valida que la funcion devuelve una lista con la misma longitud que el numero de datos en el dataframe
    def test_lecturaDB(self):
        '''Prueba la lectura de la base de datos'''
        if path.exists('././src/data/IMDB top 1000.csv'):
            df = pd.read_csv('././src/data/IMDB top 1000.csv')
            self.assertIsNotNone(df)
        else:
            raise ConnectionError("Base de datos no disponible")
    def test_comparacion(self):
        '''Prueba la funcion encargada de comparar los embeddings'''
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        df = pd.read_csv('././src/data/IMDB top 1000.csv')
        query='Heat'
        query_embedding = model.encode([query])[0]
        df['embeddings'] = aumentar_contexto(df, model)
        prueba=df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
        self.assertEqual(len(prueba),df.shape[0])#Valida que la funcion devuelva una puntuacion de similitud para cada uno de los registros de la base de datos
    def test_busquedaDB(self):
        '''Prueba de la clase encargada de realizar la busqueda de la query en la DB'''
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        df = pd.read_csv('././src/data/IMDB top 1000.csv')
        busqueda = BusquedaDB(df, model)
        self.assertEqual(len(busqueda.df['embeddings']),df.shape[0])
