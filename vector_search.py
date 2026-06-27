import chromadb
from langchain_core.documents import Document

from chunker import text_to_chunks
from embedder import embed_chunks

def store_chunks_in_chroma(chunks: list[dict]):
    """Store chunks with pre-computed embeddings in Chroma."""
    
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="rag-documents")
    
    # Prepare data
    ids = [f"{chunk['page']}_{chunk['chunk_id']}" for chunk in chunks]
    documents = [chunk['text'] for chunk in chunks]
    embeddings = [chunk['embedding'] for chunk in chunks]
    metadatas = [{"page": chunk["page"], "chunk_id": chunk["chunk_id"]} for chunk in chunks]
    
    # Add to collection
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )
    
    return collection


# s = store_chunks_in_chroma(embed_chunks(text_to_chunks()))
# print(f"Stored {len(s.get()['ids'])} chunks in ChromaDB.")