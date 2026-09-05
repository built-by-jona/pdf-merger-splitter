# PDF Merger & Splitter

A simple PDF utility built with Python and Streamlit that allows users to merge multiple PDF files into one document or extract selected pages into a new PDF.

This project is part of the **Built by J.O.N.A.** portfolio.

> **Just One Next Automation**
> Simple tools for complicated work.

## Features

### Merge PDFs

* Upload two or more PDF files
* View the page count of each uploaded file
* Merge PDFs in the order they are uploaded
* Choose a custom output filename
* Automatically adds the `.pdf` extension when needed
* Download the merged PDF directly from the app

### Split PDFs

* Upload a single PDF file
* View the total number of pages
* Extract individual pages
* Extract page ranges
* Combine individual pages and ranges in one request
* Choose a custom output filename
* Download the extracted PDF directly from the app

Supported page selection examples:

```text
1-3
1,3,5
1-3,5,7-9
```

## Built With

* Python
* Streamlit
* pypdf
* pytest

## Project Structure

```text
pdf-merger-splitter/
│
├── assets/
│   └── logo.png
│
├── sample_files/
│   ├── sample1.pdf
│   └── sample2.pdf
│
├── tests/
│   └── test_pdf_tools.py
│
├── output/
│   └── .gitkeep
│
├── app.py
├── pdf_tools.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

The application provides two PDF-processing tools.

### PDF Merger

The merger accepts multiple PDF files and processes them in upload order.

The app:

1. Validates the uploaded PDF files.
2. Reads each PDF using `pypdf`.
3. Adds the pages to a new PDF in sequence.
4. Creates the merged output file.
5. Makes the final PDF available for download.

### PDF Splitter

The splitter accepts one PDF and a page selection entered by the user.

The app:

1. Validates the uploaded PDF.
2. Reads the requested page numbers or ranges.
3. Converts the user-facing page numbers into internal page indexes.
4. Extracts the selected pages.
5. Creates a new PDF containing only those pages.
6. Makes the new PDF available for download.

## Validation and Error Handling

The application includes validation for common PDF-processing issues, including:

* No files provided
* Fewer than two PDFs provided for merging
* Missing files
* Non-PDF files
* Invalid or corrupted PDFs
* Empty page selections
* Invalid page numbers
* Page numbers outside the PDF's available range
* Invalid or reversed page ranges
* Incorrect page-selection formatting

Clear messages are displayed when processing cannot be completed.

## Testing

The project uses `pytest` for automated testing.

Run the test suite with:

```bash
python -m pytest
```

Current test coverage includes:

* Project initialization
* PDF merging
* Merge order and page counts
* Merge validation
* PDF splitting
* Page-selection parsing
* Individual page selections
* Page ranges
* Combined page selections
* Missing files
* Non-PDF files
* Corrupted PDFs
* Invalid page selections
* Boundary validation

Current status:

```text
22 passed
```

## Running the App Locally

Activate the project environment, then install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Streamlit will open the application in your browser.

## User Interface

The application uses the standard **Built by J.O.N.A.** visual identity used across the portfolio.

The interface includes:

* Navy and teal branding
* Built by J.O.N.A. logo
* Clear workflow instructions
* Separate Merge and Split tools
* PDF page-count information
* User-friendly validation messages
* Downloadable output files
* Responsive Streamlit layout

## Purpose

PDF files are frequently shared as separate documents even when they belong together, while large PDFs often contain only a few pages that someone actually needs.

This tool simplifies those everyday tasks by allowing users to combine PDFs or extract selected pages without requiring paid PDF software or complicated manual workflows.

It demonstrates practical automation using Python while keeping the user experience simple and approachable.

## Portfolio

**Built by J.O.N.A.** focuses on small practical tools designed to solve everyday business and administrative problems.

**J.O.N.A.** stands for:

**Just One Next Automation**

> Simple tools for complicated work.

## Project Status

✅ PDF merge functionality complete
✅ PDF split functionality complete
✅ Input validation complete
✅ Automated testing complete
✅ Streamlit interface complete
✅ Built by J.O.N.A. branding complete
✅ Ready for deployment