import pandas as pd
from sentence_transformers import SentenceTransformer,util

def compute_similarity(example, query_embedding):
    embedding = example['embeddings'] 
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity  
def aumentar_contexto(df,model):
    combined_text = df.apply(lambda row: ' '.join([str(row['Description']), str(row['Title']), str(row['Genre'])]), axis=1)  
    embeddings = model.encode(combined_text.tolist(), batch_size=64, show_progress_bar=True)
    return embeddings 

def main(query,df):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings=aumentar_contexto(df,model)
    df['embeddings'] = embeddings.tolist()
    query_embedding = model.encode([query])[0]
    df['similarity'] = df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
    df = df.sort_values(by='similarity', ascending=False)
    print("Los resultados de la busqueda son:")
    print(df.head()[['Title','Description']])



if __name__ == '__main__':
    print("Esta es una muestra de las peliculas en la base de datos:")
    df = pd.read_csv('./semantic_search/IMDB top 1000.csv')
    print(df.head())
    while(True):
        query = input("ingresa el termino de busqueda, oprimir enter con el camppo de busqueda vacio para detener el programa: ")
        if query=="":
            print("Deteniendo el programa")
            break
        else:
            main(query,df)