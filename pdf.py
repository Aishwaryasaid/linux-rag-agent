from pypdf import PdfReader


#remove max_pages argument to run on all pages of the PDF
def pdf_to_text(max_pages=10) : 
    pdf_path = "Linux.pdf"
    """Extract text from all pages of a PDF.
       
       Args:
           pdf_path: Path to the PDF file
           
       Returns:
           Dictionary with page numbers as keys and extracted text as values
       """
    # creating a pdf reader object
    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None
    
    
    reader = PdfReader(pdf_path)

    pdf_text_dict = {}
    
    # Limit pages if max_pages is set
    total_pages = len(reader.pages)
    pages_to_process = min(max_pages, total_pages) if max_pages else total_pages
    
    for index in range(pages_to_process):
        page_no = index + 1
        pdf_text_dict[page_no] = reader.pages[index].extract_text()
    
    return pdf_text_dict

    # loop through all the pages and extract text
    # pdf_text_dict = {}
    # # loop through all the pages and extract text
    # for index,page in enumerate(reader.pages):
    #     page_no = index+1 
    #     pdf_text_dict[page_no] = page.extract_text()
    # return pdf_text_dict  # Return text of the first page
    


