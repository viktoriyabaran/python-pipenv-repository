import pandas as pd

def console_output(text: str) -> None:
    """
    Enables input from console, returns the user input.

    Args:
        text (str): Text for output

    Returns: None
    """
    print(text)

def write_to_file(file_path: str, text: str) -> None:
    """
    Writes text to the file with the given path

    Args:
        file_path (str): Relative or absolute path to the file

    Returns: None
    """
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(text + "\n")
 