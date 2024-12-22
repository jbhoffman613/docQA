''' Functions to extract and process .docx files using the python-docx library '''
from docx import Document

def open_docx(file_path):
    ''' Open a .docx file and return a Document object '''
    return Document(file_path)

def extract_text(doc: Document):
    ''' Extract text from a Document object '''
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def fname_to_text(file_path):
    ''' Open a .docx file and extract text '''
    return extract_text(open_docx(file_path))

if __name__ == "__main__":
    fname = "/Users/hoffmanj/projects/docQA/docqa/doc_extraction/documents/ca_location_agreement.docx"
    print(fname_to_text(file_path=fname))
