import pytest
from fpdf import FPDF
from tempfile import NamedTemporaryFile
import os


@pytest.fixture
def generate_pdf_file():
    with NamedTemporaryFile(suffix=".pdf", mode="wb", delete=False) as temp_file:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200,100, txt="This is a sample document", align="C")
        pdf.output(temp_file.name)

    yield temp_file.name

    os.remove(temp_file.name)