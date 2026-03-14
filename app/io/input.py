import pandas as pd

def console_input() -> str:
    """
    Enables input from console, returns the user input.

    Args: None

    Returns: 
        text (str): User input
    """
    text = input("Input text: ")
    return text

def read_file(file_path: str) -> str:
    """
    Reads and returns text from the file with the given path

    Args:
        file_path (str): Relative or absolute path to the CSV file

    Returns: 
        test (str): Text read from the file
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        return text
    
def read_file_pandas(file_path: str) -> pd.DataFrame:
    """
    Reads data from a CSV file using the pandas library.

    Args:
        file_path (str): Relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: Data read from the file as a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    print(type(df))
    return df