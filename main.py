from rag_agent import RAGAgent

def main():
    # 1. Initialize
    print("Loading PDF and building RAG system...")
    agent = RAGAgent("linux.pdf")
    print("✅ Ready!\n")
    
    # 2. Loop for multiple questions
    while True:
        # 3. Get user input
        question = input("Ask a question (or 'quit' to exit): ").strip()
        
        if question.lower() == "quit":
            print("Goodbye!")
            break
        
        if not question:
            print("Please enter a question.\n")
            continue
        
        # 4. Get answer
        print("\n🔍 Searching and thinking...\n")
        answer = agent.ask(question)
        
        # 5. Display result
        print(answer)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()