<p align="center">
  <img src="assets/banner.png" alt="Built by J.O.N.A." width="100%">
</p>

<h1 align="center">PDF Merger & Splitter</h1>

<p align="center">
  <strong>Built by J.O.N.A.</strong><br>
  <em>Simple tools for complicated work.</em>
</p>

<p align="center">
  <strong>🚀 Live Demo — Coming Soon</strong>
</p>

---

## Overview

The **PDF Merger & Splitter** is a Python application that makes it easy to combine multiple PDF files into one document or extract selected pages from an existing PDF.

Instead of using separate tools or manually managing PDF pages, users can upload their files, choose whether to merge or split them, and download the resulting PDF directly from the application.

This is the **fourth completed project** in my **Built by J.O.N.A.** portfolio—a collection of practical automation tools designed to simplify repetitive business tasks.

---

## Why I Built This

PDF files are commonly used for invoices, reports, forms, contracts, supporting documents, and other business records.

Sometimes several separate PDFs need to be combined into one document. Other times, a large PDF contains only a few pages that actually need to be shared or saved.

These tasks are simple, but they can become repetitive when they happen regularly.

This project demonstrates how Python can automate basic PDF organization while keeping the process simple for the user.

---

## Business Problem

Managing PDF documents often involves:

- Combining several related PDFs into one file
- Extracting only specific pages from a larger document
- Using separate software for simple PDF tasks
- Repeating the same document-processing steps
- Manually checking page numbers
- Managing output filenames
- Spending unnecessary time on basic file preparation

These small document-management tasks can add unnecessary administrative work over time.

---

## Solution

The PDF Merger & Splitter enables users to:

- Upload multiple PDFs for merging
- Combine PDFs in upload order
- View the number of pages in uploaded files
- Upload a PDF for page extraction
- Select individual pages
- Select page ranges
- Combine individual pages and ranges
- Choose custom output filenames
- Download the processed PDF directly from the application

Examples of supported page selections:

```text
1-3
1,3,5
1-3,5,7-9
```

---

## Features

### PDF Merging

- Upload two or more PDF files
- View the page count of each uploaded PDF
- Merge PDFs in upload order
- Create a single combined PDF
- Choose a custom output filename
- Automatically add the `.pdf` extension when needed

### PDF Splitting

- Upload a single PDF
- View the total number of pages
- Extract individual pages
- Extract page ranges
- Combine individual pages and ranges
- Create a new PDF containing only selected pages

### Page Selection

The splitter supports flexible page-selection formats.

Examples:

```text
1-3
2,4,6
1-3,5,7-9
```

User-facing page numbers begin at page 1, making page selection straightforward.

### Validation & Error Handling

- Requires at least two PDFs for merging
- Detects missing files
- Rejects non-PDF files
- Handles invalid or corrupted PDFs
- Detects empty page selections
- Validates individual page numbers
- Prevents pages outside the available range
- Detects invalid page ranges
- Rejects reversed page ranges
- Handles incorrect page-selection formatting

### Output

- Uploaded PDF page-count information
- Custom output filenames
- Downloadable merged PDFs
- Downloadable extracted PDFs
- Clear success and validation messages

---

## Technology Stack

- Python
- Streamlit
- pypdf
- Pytest
- Git
- GitHub

---

## Project Structure

```text
pdf-merger-splitter/
│
├── assets/
│   ├── banner.png
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
│
├── app.py
├── pdf_tools.py
├── CHANGELOG.md
├── pytest.ini
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Project Status

**Version:** 1.0

**Status:** ✅ Complete

The first release includes:

- PDF merge functionality
- PDF split functionality
- Flexible page-selection parsing
- PDF page-count display
- Custom output filenames
- Automatic `.pdf` extension handling
- Streamlit web application
- Downloadable processed PDFs
- Validation and error handling
- Automated testing with Pytest
- Built by J.O.N.A. branded interface
- Project documentation

Current automated test suite:

```text
22 passed
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/built-by-jona/pdf-merger-splitter.git
```

### Create the Conda environment

```bash
conda create -n pdf-merger-splitter python
```

### Activate the environment

```bash
conda activate pdf-merger-splitter
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the tests

```bash
pytest
```

### Launch the application

```bash
streamlit run app.py
```

---

## Current Limitations

The current version focuses on straightforward PDF merging and page extraction.

Some limitations include:

- Uploaded PDFs cannot currently be reordered through drag-and-drop
- Password-protected PDFs are not supported
- PDF pages cannot be visually previewed before extraction
- Pages cannot be rearranged within the splitter
- The splitter creates one output PDF from the selected pages rather than multiple separate PDFs
- Very large PDF files may be limited by available system or hosting resources

The project intentionally focuses on simple, reliable PDF processing rather than advanced PDF editing.

---

## Future Enhancements

Future versions may include:

- Drag-and-drop PDF reordering
- PDF page previews
- Visual page selection
- Page rearrangement
- Extracting selected pages into separate PDF files
- Removing selected pages from a PDF
- PDF rotation
- Batch PDF splitting
- ZIP downloads for multiple output files
- Improved handling of large PDF documents
- Additional PDF organization tools

---

## What I Learned

Building this project strengthened my skills in:

- PDF processing with Python
- Merging PDF documents programmatically
- Extracting selected PDF pages
- Parsing user-entered page ranges
- Converting user-facing page numbers into internal indexes
- File and folder handling
- Temporary file management
- Input validation and error handling
- Building interactive applications with Streamlit
- Writing automated tests with Pytest
- Structuring reusable Python modules
- Version control with Git and GitHub
- Maintaining consistent branding across multiple portfolio projects

It also reinforced an important development principle:

> A simple tool becomes much more useful when it handles incorrect input clearly and safely.

---

## About Built by J.O.N.A.

**J.O.N.A.** stands for **Just One Next Automation**.

Built by J.O.N.A. is my personal portfolio focused on creating practical automation tools that simplify repetitive work and solve real business problems.

Every project is built with the same philosophy:

- Solve a real problem.
- Keep the solution simple.
- Build something reliable.
- Keep improving.

> **Simple tools for complicated work.**