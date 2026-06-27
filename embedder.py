from langchain_ollama import OllamaEmbeddings
from chunker import text_to_chunks

def embed_chunks(chunks: list[dict]) -> list[dict]:
    """Generate embeddings for text chunks using Ollama.
    
    Args:
        chunks: List of dicts with 'page', 'chunk_id', 'text'
        
    Returns:
        Same list of dicts, but with 'embedding' key added to each
    """
    # 1. Create OllamaEmbeddings object with "nomic-embed-text"
    embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434" # Default Ollama URL
    )

    # 2. Loop through each chunk
    for chunk in range(len(chunks)):
        chunk_text = chunks[chunk]['text']
        # Generate embedding for this chunk's text
        try:
            embedding_vector = embeddings.embed_query(chunk_text)
        except Exception as e:
            print(f"Error generating embedding for chunk {chunk}: {e}")
            continue
        # Add the embedding to the chunk dict
        chunks[chunk]['embedding'] = embedding_vector
    return chunks

# e = embed_chunks(text_to_chunks())
# print(e)