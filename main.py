from app import (
    console_input,
    read_file,
    read_file_pandas,
    console_output,
    write_to_file
)

def main():
    output_file = "data/output.txt"

    text_console = console_input()
    write_to_file(output_file, text_console)

    text_file = read_file("data/input.txt")
    write_to_file(output_file, text_file)

    df = read_file_pandas("data/input.csv")
    write_to_file(output_file, df.to_string())

    output_file_content = read_file(output_file)
    print("\nOutput file content: ")
    console_output(output_file_content)


if __name__ == '__main__':
    main()