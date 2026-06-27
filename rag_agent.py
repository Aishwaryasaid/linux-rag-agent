from pdf import pdf_to_text
from chunker import text_to_chunks
from embedder import embed_chunks
from vector_search import store_chunks_in_chroma
from retriever import retrieve_chunks
from llm_answer import llm_answer

class RAGAgent:
    def __init__(self, pdf_path: str):
        """Initialize RAG agent with a PDF."""
        # Build the pipeline
        chunks = text_to_chunks()  # Already hardcoded pdf_path
        embedded = embed_chunks(chunks)
        self.collection = store_chunks_in_chroma(embedded)
    
    def ask(self, question: str) -> str:
        """Ask a question and get an answer."""
        # Retrieve
        chunks = retrieve_chunks(self.collection, question, k=3)
        
        # Generate
        result = llm_answer(chunks, question)
        
        # Format pretty (Option B)
        answer_text = result["answer"]
        pages = ", ".join([str(p) for p in result["pages"]])
        
        formatted = f"""=== ANSWER ===
{answer_text}

📄 Source Pages: {pages}"""
        
        return formatted
    
    
r = RAGAgent(pdf_path="Linux.pdf")
print(r.ask("What is the difference between a process and a thread?"))