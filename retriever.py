from langchain_ollama import OllamaEmbeddings
import chromadb
from embedder import embed_chunks
from chunker import text_to_chunks
from vector_search import store_chunks_in_chroma
def retrieve_chunks(collection, question: str, k: int = 5) -> list[dict]:
    """
    Search Chroma for chunks similar to the question.
    
    Args:
        collection: Chroma collection object (from Step 4)
        question: User's question string
        k: Number of top chunks to return (default 5)
        
    Returns:
        List of dicts with 'text', 'page', 'chunk_id'
    """
    
    # 1. Create same embedding model as Step 3
    embedding_function = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://localhost:11434"
    )
    
    # 2. Convert question to embedding
    question_embedding = embedding_function.embed_query(question)
    
    # 3. Search Chroma for top K similar chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=k
    )
    
    # 4. Format results into list of dicts
    retrieved_chunks = [
        {
            "text": results['documents'][0][i],
            "page": results['metadatas'][0][i]['page'],
            "chunk_id": results['metadatas'][0][i]['chunk_id']
        }
        for i in range(len(results['documents'][0]))
    ]
    
    return retrieved_chunks

r = retrieve_chunks(store_chunks_in_chroma(embed_chunks(text_to_chunks())), "What is Linux?", k=3)
print(r)