from parser.utils import read_uploaded_file


def test_read_uploded_pdf_file(generate_pdf_file):
    with open(generate_pdf_file, "rb") as file_object:
        test_result = read_uploaded_file(file_object,"pdf")
        assert test_result == "This is a sample document\n"
