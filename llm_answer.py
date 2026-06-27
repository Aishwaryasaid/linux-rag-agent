from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

def llm_answer(chunks: list[dict], question: str) -> dict:
    """Generate an answer using context."""
    
    chat_model = ChatOllama(model="llama3.2")
    
    context = "\n\n".join([f"Page {chunk['page']}: {chunk['text']}" for chunk in chunks])
    
    # Use system + user messages (better!)
    messages = [
        SystemMessage(content="""You are a helpful assistant. You MUST answer ONLY based on the provided context. 
If the context doesn't contain the answer, say: 'I cannot find this information in the provided document.'
Do NOT use your own knowledge. Only use what is given in the context."""),
        HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}")
    ]
    
    answer = chat_model.invoke(messages)
    pages = [chunk['page'] for chunk in chunks]
    
    return {
        "answer": answer.content,
        "pages": pages
    }