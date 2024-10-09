import pandas as pd
from sentence_transformers import SentenceTransformer,util

def compute_similarity(example, query_embedding):
    #Esta función compara los embeddings y retorna un valor con la similitud semantica entre ellos
    embedding = example['embeddings'] 
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity  
def aumentar_contexto(df,model):
    #Esta función aumenta los campos de la base de datos con los que se crean los embeddings
    combined_text = df.apply(lambda row: ' '.join([str(row['Description']), str(row['Title']), str(row['Genre'])]), axis=1)  
    embeddings = model.encode(combined_text.tolist(), batch_size=64, show_progress_bar=True)
    return embeddings 

def main(query,df):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')#Seleccion del modelo que se utilizara para transformar el lenguaje en embedings
    embeddings=aumentar_contexto(df,model)
    df['embeddings'] = embeddings.tolist()
    query_embedding = model.encode([query])[0] #Se transforma la busqueda ingresada por el usuario en un embedding para compararlo con los embeddings que se obtienen de la base de datos
    df['similarity'] = df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
    df = df.sort_values(by='similarity', ascending=False)# Se ordenan los resultados en base a la similitud con la busqueda realizada por el usuario
    print("Los resultados de la busqueda son:")
    print(df.head()[['Title','Description']])



if __name__ == '__main__':
    print("Esta es una muestra de las peliculas en la base de datos:")
    df = pd.read_csv('./semantic_search/IMDB top 1000.csv')
    print(df.head())
    while(True):
        query = input("ingresa el termino de busqueda, oprimir enter con el campo de busqueda vacio para detener el programa: ")
        if query=="":
            print("Deteniendo el programa")
            break
        else:
            main(query,df)