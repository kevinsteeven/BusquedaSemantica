import pandas as pd
from sentence_transformers import SentenceTransformer,util
import os.path as path#libreria importada para validar excepcion de si no se encuentra el archivo. documentacion: https://docs.python.org/es/3.10/library/os.html



def compute_similarity(example, query_embedding):
    #Esta función compara los embeddings y retorna un valor con la similitud semantica entre ellos, esta función cumple con el principio de single responsability
    embedding = example['embeddings'] 
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity  
def aumentar_contexto(df,model):
    #Esta función aumenta los campos de la base de datos con los que se crean los embeddings y devuelve una lista con estos embeddings, el modelo se envia como entrada para cumplir con el principio de dependency inversion
    combined_text = df.apply(lambda row: ' '.join([str(row['Description']), str(row['Title']), str(row['Genre'])]), axis=1)  
    embeddings = model.encode(combined_text.tolist(), batch_size=64, show_progress_bar=True)
    return embeddings.tolist()
def validar_fin(query):
    #Esta función valida si se debe detener el programa o proceder a procesar la consulta, esta función cumple con el principio de single responsability
    if query=="":
            print("Deteniendo el programa")
            return True
    else:
            return False
class BusquedaDB():
    #Se sigue el patron de diseño Facade creando una fachada que simplifica el proceso realizado por el programa llamando internamente las funciones involucradas en el proceso
    def __init__(self,df,model):#Inicializa la instancia creando el dataframe com los embeddings de los campos de la base de datos
        self.df = df  
        self.model = model
        self.df['embeddings'] = aumentar_contexto(df, model) 
    def ejecutar_busqueda(self,query):#Vectoriza la consulta del usuario e invoca a la funcion encargada de comparar con los embeddings de la base de datos
        query_embedding = self.model.encode([query])[0]
        self.df['similarity'] = self.df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
        self.df = self.df.sort_values(by='similarity', ascending=False)# Se ordenan los resultados en base a la similitud con la busqueda realizada por el usuario
        return self.df
def main():
    print("Esta es una muestra de las peliculas en la base de datos:")
    if path.exists('./src/data/IMDB top 1000.csv'):
        df = pd.read_csv('./src/data/IMDB top 1000.csv')#Lectura de base de datos
    else: 
        raise ConnectionError("Base de datos no disponible")#Manejo de excepcion si no se encuentra el archivo
    print(df.head())
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')#Seleccion del modelo que se utilizara para transformar el lenguaje en embedings
    fin=False
    while(fin==False):
        query = input("ingresa el termino de busqueda, oprimir enter con el campo de busqueda vacio para detener el programa: ")
        fin=validar_fin(query)
        if fin == False:
          procesobusqueda=BusquedaDB(df,model)# La clase busqueda es una fachada que se encarga internamente de vectorizar los strings y hacer la comparacion
          df=procesobusqueda.ejecutar_busqueda(model,query)
          print("Los resultados de la busqueda son:")
          print(df.head()[['Title','Description']])

if __name__ == '__main__':
    main()
