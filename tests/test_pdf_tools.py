from pathlib import Path

import pytest
from pypdf import PdfReader, PdfWriter

from pdf_tools import (
    merge_pdfs,
    parse_page_selection,
    project_status,
    split_pdf,
)
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

def test_parse_page_range():
    result = parse_page_selection("1-3", 5)

    assert result == [0, 1, 2]


def test_parse_multiple_pages():
    result = parse_page_selection("1,3,5", 5)

    assert result == [0, 2, 4]


def test_parse_combined_selection():
    result = parse_page_selection("1-2,4,6-7", 7)

    assert result == [0, 1, 3, 5, 6]


def test_parse_invalid_page():
    with pytest.raises(ValueError):
        parse_page_selection("1-6", 5)


def test_parse_invalid_range():
    with pytest.raises(ValueError):
        parse_page_selection("4-2", 5)


def test_split_pdf(tmp_path):
    source_pdf = tmp_path / "source.pdf"
    output_pdf = tmp_path / "split.pdf"

    create_test_pdf(source_pdf, 5)

    result = split_pdf(
        source_pdf,
        "2-4",
        output_pdf,
    )

    assert result == output_pdf
    assert output_pdf.exists()

    reader = PdfReader(str(output_pdf))
    assert len(reader.pages) == 3


def test_split_selected_pages(tmp_path):
    source_pdf = tmp_path / "source.pdf"
    output_pdf = tmp_path / "split.pdf"

    create_test_pdf(source_pdf, 6)

    split_pdf(
        source_pdf,
        "1,3,6",
        output_pdf,
    )

    reader = PdfReader(str(output_pdf))
    assert len(reader.pages) == 3


def test_split_missing_file(tmp_path):
    missing_pdf = tmp_path / "missing.pdf"
    output_pdf = tmp_path / "split.pdf"

    with pytest.raises(FileNotFoundError):
        split_pdf(
            missing_pdf,
            "1",
            output_pdf,
        )