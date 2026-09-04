from pathlib import Path

from pypdf import PdfReader, PdfWriter


def project_status():
    """Return the current project status."""
    return "PDF Merger & Splitter initialized"


def merge_pdfs(input_files, output_file):
    """
    Merge multiple PDF files into one PDF.

    Args:
        input_files: A list of PDF file paths.
        output_file: Path for the merged output PDF.

    Returns:
        Path to the created merged PDF.

    Raises:
        ValueError: If fewer than two PDF files are provided.
        FileNotFoundError: If any input file does not exist.
    """
    if len(input_files) < 2:
        raise ValueError("At least two PDF files are required to merge.")

    writer = PdfWriter()

    for file_path in input_files:
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}")

        reader = PdfReader(str(file_path))

        for page in reader.pages:
            writer.add_page(page)

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)

    return output_file

def parse_page_selection(selection, total_pages):
    """
    Convert a page selection string into zero-based page indexes.

    Examples:
        "1-3" -> [0, 1, 2]
        "2,4,6" -> [1, 3, 5]
        "1-3,5,7-8" -> [0, 1, 2, 4, 6, 7]
    """
    if not selection or not selection.strip():
        raise ValueError("Page selection cannot be empty.")

    pages = []

    for part in selection.split(","):
        part = part.strip()

        if "-" in part:
            start_text, end_text = part.split("-", 1)

            try:
                start = int(start_text)
                end = int(end_text)
            except ValueError:
                raise ValueError(f"Invalid page range: {part}")

            if start > end:
                raise ValueError(f"Invalid page range: {part}")

            for page_number in range(start, end + 1):
                if page_number < 1 or page_number > total_pages:
                    raise ValueError(
                        f"Page {page_number} is outside the PDF page range."
                    )

                pages.append(page_number - 1)

        else:
            try:
                page_number = int(part)
            except ValueError:
                raise ValueError(f"Invalid page number: {part}")

            if page_number < 1 or page_number > total_pages:
                raise ValueError(
                    f"Page {page_number} is outside the PDF page range."
                )

            pages.append(page_number - 1)

    return pages


def split_pdf(input_file, page_selection, output_file):
    """
    Extract selected pages from a PDF into a new PDF.

    Args:
        input_file: Path to the source PDF.
        page_selection: Pages to extract, e.g. "1-3,5,7".
        output_file: Path for the new PDF.

    Returns:
        Path to the created PDF.
    """
    input_file = Path(input_file)

    if not input_file.exists():
        raise FileNotFoundError(f"PDF file not found: {input_file}")

    reader = PdfReader(str(input_file))
    total_pages = len(reader.pages)

    selected_pages = parse_page_selection(
        page_selection,
        total_pages,
    )

    writer = PdfWriter()

    for page_index in selected_pages:
        writer.add_page(reader.pages[page_index])

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)

    return output_file