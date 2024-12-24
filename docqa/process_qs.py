''' Processes a list of questions for a specific document '''
import pandas as pd
from docqa import iollama

def csv_to_dataframe(fname: str) -> pd.DataFrame:
    ''' Converts a CSV to a dataframe '''
    df = pd.read_csv(fname)
    return df

def df_to_qs(df: pd.DataFrame) -> list:
    ''' Pulls out the column of questions '''
    qs = df["Question"].tolist()
    return qs

def get_qs(fname: str) -> list:
    ''' Returns the questions from a CSV file '''
    qs = df_to_qs(csv_to_dataframe(fname))
    return qs

def get_answers(fname_csv: str, fdoc: str) -> dict:
    ''' Given a document name and a CSV of questions, 
    return a dict with all the question/answer pairs
    
    Input:
        fname_csv: The the file name of the CSV file
        fdoc: The file name of the legal you want to understand'''
    qs: list = get_qs(fname=fname_csv)
    answers: dict = {}
    for i, question in enumerate(qs):
        print(f"Now running question #{i+1}")
        # Generate the answer for a document/question pair
        answers[question] = iollama.fname_and_q(fname=fdoc, question=question)
    return answers

def save_questions(fname: str, pairs: dict) -> pd.DataFrame:
    ''' Takes a dictionary of information and saves it to a CSV '''
    # Create the properly formatted dataframe
    new_df = pd.DataFrame(pairs.items())
    new_df = new_df.rename(columns={0: "question", 1: "answer"})

    # Create and save the CSV file
    final_fname = f"{fname}.csv"
    new_df.to_csv(final_fname)

    # Print and return the dataframe
    print("The final question/answer set is: \n")
    print(new_df)
    return new_df

def make_save_answers(fqs: str, fdoc: str, fsave: str) -> pd.DataFrame:
    ''' Given a CSV of questions, a document, and a save name, 
    return a dataframe of the question/answer pairs and save it to a CSV '''
    # Generate the question/answer pairs
    answers = get_answers(fname_csv=fqs, fdoc=fdoc)

    # Save the question/answer pairs to a CSV
    return save_questions(fname=fsave, pairs=answers)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--fdoc",
                    type=str,
                    default=("/Users/hoffmanj/projects/docQA/docqa/"
                                + "documents/winton_safeco_umbrella_policy.pdf"))
    parser.add_argument("--fcsv_qs", type=str, default=("/Users/hoffmanj/projects/"
                                                        + "docQA/docqa/documents/pdf_qs.csv"))
    parser.add_argument("--fcsv_save", type=str, default="safeco_umbrella_generated_qa")

    args = parser.parse_args()

    # Run the main function
    FDOC_NAME = args.fdoc
    FQS = args.fcsv_qs
    FSAVE_NAME = args.fcsv_save

    make_save_answers(fqs=FQS, fdoc=FDOC_NAME, fsave=FSAVE_NAME)
