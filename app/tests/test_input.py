import pandas as pd
from ..io import read_file, read_file_pandas

def test_read_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("hello world", encoding="utf-8")

    result = read_file(file)

    assert result == "hello world"

def test_read_file_pandas(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("name,age\nAlice,20\nBob,21", encoding="utf-8")

    df = read_file_pandas(file)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)