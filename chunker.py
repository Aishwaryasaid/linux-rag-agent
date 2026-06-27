from pdf import pdf_to_text
from langchain_text_splitters import RecursiveCharacterTextSplitter


def text_to_chunks():
    
    """Chunk text from PDF pages into overlapping segments.
    
    Returns:
        List of dicts with keys: page, chunk_id, text
    """
    
    # 1.Text extraction from PDF
    pages_dict = pdf_to_text()
    
    ## 2. Initialize the splitter
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # Maximum number of characters per chunk
    chunk_overlap=100,     # Number of characters shared between adjacent chunks
    length_function=len   # Built-in python len function to count characters
    )
    
    
    
    
    # Step 3: Loop through each page and chunk
    all_documents = []
    chunk_id = 0
    
    for page_num, text in pages_dict.items():
        # Chunk this page's text
        chunks = splitter.split_text(text)
        
        # For each chunk, create a document with metadata
        for chunk_text in chunks:
            doc = {
                "page": page_num,
                "chunk_id": chunk_id,
                "text": chunk_text
            }
            all_documents.append(doc)
            chunk_id += 1
    
    return all_documents

# # Test it
# chunks = text_to_chunks()
# for chunk in chunks[:2]:  # Print first 2
#     print(chunk)

