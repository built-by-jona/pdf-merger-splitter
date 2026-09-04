from pathlib import Path

import pytest
from pypdf import PdfReader, PdfWriter

from pdf_tools import merge_pdfs, project_status


def create_test_pdf(file_path, page_count=1):
    """Create a simple blank PDF for testing."""
    writer = PdfWriter()

    for _ in range(page_count):
        writer.add_blank_page(width=612, height=792)

    with open(file_path, "wb") as pdf_file:
        writer.write(pdf_file)


def test_project_status():
    assert project_status() == "PDF Merger & Splitter initialized"


def test_merge_two_pdfs(tmp_path):
    first_pdf = tmp_path / "first.pdf"
    second_pdf = tmp_path / "second.pdf"
    output_pdf = tmp_path / "merged.pdf"

    create_test_pdf(first_pdf, 2)
    create_test_pdf(second_pdf, 3)

    result = merge_pdfs(
        [first_pdf, second_pdf],
        output_pdf,
    )

    assert result == output_pdf
    assert output_pdf.exists()

    reader = PdfReader(str(output_pdf))
    assert len(reader.pages) == 5


def test_merge_requires_two_pdfs(tmp_path):
    single_pdf = tmp_path / "single.pdf"
    output_pdf = tmp_path / "merged.pdf"

    create_test_pdf(single_pdf)

    with pytest.raises(
        ValueError,
        match="At least two PDF files are required",
    ):
        merge_pdfs([single_pdf], output_pdf)


def test_merge_missing_file(tmp_path):
    existing_pdf = tmp_path / "existing.pdf"
    missing_pdf = tmp_path / "missing.pdf"
    output_pdf = tmp_path / "merged.pdf"

    create_test_pdf(existing_pdf)

    with pytest.raises(FileNotFoundError):
        merge_pdfs(
            [existing_pdf, missing_pdf],
            output_pdf,
        )