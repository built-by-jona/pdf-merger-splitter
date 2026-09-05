# Changelog

All notable changes to the **PDF Merger & Splitter** project are documented in this file.

This project is part of the **Built by J.O.N.A.** portfolio.

## [1.0.0] - 2026-09-05

### Added

* Initial Python project structure
* PDF processing module
* PDF merge functionality
* PDF split functionality
* Page-selection parser
* Support for individual page selections such as `1,3,5`
* Support for page ranges such as `1-3`
* Support for combined selections such as `1-3,5,7-9`
* Automatic output directory creation
* Custom output filenames
* Automatic `.pdf` extension handling
* PDF page-count display
* Streamlit web interface
* Separate Merge PDFs and Split PDF tools
* Downloadable merged PDF files
* Downloadable extracted PDF files
* Built by J.O.N.A. navy-and-teal interface
* Built by J.O.N.A. logo and portfolio branding
* Responsive interface styling
* User-friendly instructions and status messages
* Automated pytest test suite
* `pytest.ini` project configuration
* Sample PDF files for development and testing
* Project README
* Project changelog

### Validation

Added validation and error handling for:

* Empty merge requests
* Fewer than two PDFs when merging
* Missing PDF files
* Non-PDF files
* Invalid or corrupted PDF files
* Empty page selections
* Invalid page numbers
* Page numbers outside the available PDF range
* Invalid page ranges
* Reversed page ranges
* Incorrect page-selection formatting

### Testing

* Added automated tests for PDF merging
* Added automated tests for PDF splitting
* Added tests for page-selection parsing
* Added tests for file validation
* Added tests for corrupted and non-PDF files
* Added tests for invalid page selections
* Final test suite status: **22 passed**

### User Interface

* Added PDF Merger & Splitter branded header
* Added Built by J.O.N.A. logo
* Added navy-and-teal portfolio styling
* Added workflow instructions
* Added PDF upload cards
* Added page-count information
* Added custom filename inputs
* Added full-width processing and download buttons
* Added Built by J.O.N.A. footer

### Branding

**Built by J.O.N.A.**

**Just One Next Automation**

*Simple tools for complicated work.*

### Status

Version 1.0.0 represents the first complete portfolio release of **PDF Merger & Splitter**.
