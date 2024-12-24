''' Extract text from a .docx, .pdf, or .txt file '''
import re
import pypdf
from docx import Document

def fname_to_text(file_path):
    ''' Open a .docx file and extract text '''
    text = ""
    if re.search(r".docx", file_path):
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    elif re.search(r".pdf", file_path):
        reader = pypdf.PdfReader(file_path)
        for _, page in enumerate(reader.pages):
            text += page.extract_text()
            text += "\n"
        return text
    elif re.search(r".txt", file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

if __name__ == "__main__":
    # fname = "/Users/hoffmanj/projects/docQA/docqa/doc_extraction/documents/ca_location_agreement.docx"
    # print(fname_to_text(file_path=fname))

    import argparse

    # Parse Arguments
    parser = argparse.ArgumentParser()
    # parser.add_argument("--fname",
    #                     type=str,
    #                     default=("/Users/hoffmanj/projects/docQA/docqa/"
    #                              + "doc_extraction/documents/ca_location_agreement.docx"))
    parser.add_argument("--fname",
                        type=str,
                        default=("/Users/hoffmanj/projects/docQA/docqa/"
                                 + "doc_extraction/documents/winton_safeco_auto_policy.pdf"))

    # Parse args
    args = parser.parse_args()
    FN = args.fname

    # Extract text from file
    EXTRACTED_TEXT = fname_to_text(file_path=FN)
    print(EXTRACTED_TEXT)
