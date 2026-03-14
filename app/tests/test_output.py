from ..io import write_to_file

def test_write_to_file(tmp_path):
    file = tmp_path / "test.txt"

    write_to_file(file, "hello")

    content = file.read_text(encoding="utf-8")
    assert "hello" in content