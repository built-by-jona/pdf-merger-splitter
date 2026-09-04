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