''' Ollama wrapper functions '''
from langchain_ollama import OllamaLLM
# import docqa.doc_extraction.docx_file as docx_file
import docqa.text_extractor as text_extractor


LLM = OllamaLLM(model="llama3")

def query_ollama(text: str="Why is the sky blue?"):
    ''' Query the Ollama model with a text string '''
    return LLM.invoke(text)

def fname_and_q(fname: str, question: str):
    ''' Extract text from a .docx file and query Ollama with a question '''
    answer = text_extractor.fname_to_text(fname) + "\n\n" + question
    return query_ollama(answer)

if __name__ == "__main__":
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
                                 + "doc_extraction/documents/winton_safeco_umbrella_policy.pdf"))
    parser.add_argument("--question",
                        type=str,
                        default=("Can you please summarize this document"
                                 + " in language that a highschooler could understand?"))
    args = parser.parse_args()

    # Run test functions
    FN = args.fname
    Q = args.question

    print("File Name: ", FN)
    print("Question: ", Q)
    print("Now querying Ollama...\n")
    print("Answer: ")
    ANSWER = fname_and_q(fname=FN, question=Q)
    print(ANSWER)
