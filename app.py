import tempfile
from pathlib import Path

import streamlit as st
from pypdf import PdfReader

from pdf_tools import merge_pdfs, split_pdf


st.set_page_config(
    page_title="PDF Merger & Splitter",
    page_icon="📄",
    layout="centered",
)


def clean_pdf_filename(filename, default_name):
    """Return a safe PDF filename."""
    filename = filename.strip()

    if not filename:
        filename = default_name

    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"

    return filename


def get_pdf_page_count(uploaded_file):
    """Return the number of pages in an uploaded PDF."""
    try:
        uploaded_file.seek(0)
        reader = PdfReader(uploaded_file)
        page_count = len(reader.pages)
        uploaded_file.seek(0)

        return page_count

    except Exception:
        uploaded_file.seek(0)
        return None


st.title("PDF Merger & Splitter")

st.write(
    "Combine multiple PDF files into one document "
    "or extract only the pages you need."
)


tab_merge, tab_split = st.tabs(
    [
        "Merge PDFs",
        "Split PDF",
    ]
)


with tab_merge:
    st.subheader("Merge PDFs")

    st.write(
        "Upload two or more PDF files. "
        "They will be merged in the order shown below."
    )

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        key="merge_files",
    )

    if uploaded_files:
        st.info(
            f"{len(uploaded_files)} PDF file(s) selected."
        )

        for index, uploaded_file in enumerate(
            uploaded_files,
            start=1,
        ):
            page_count = get_pdf_page_count(uploaded_file)

            if page_count is not None:
                st.write(
                    f"{index}. {uploaded_file.name} "
                    f"— {page_count} page(s)"
                )

            else:
                st.write(
                    f"{index}. {uploaded_file.name}"
                )

    merge_filename = st.text_input(
        "Merged file name",
        value="merged.pdf",
        key="merge_filename",
    )

    if st.button(
        "Merge PDFs",
        type="primary",
        key="merge_button",
        use_container_width=True,
    ):
        if not uploaded_files:
            st.error(
                "Please upload at least two PDF files."
            )

        elif len(uploaded_files) < 2:
            st.error(
                "At least two PDF files are required."
            )

        else:
            try:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_dir = Path(temp_dir)

                    input_paths = []

                    for index, uploaded_file in enumerate(
                        uploaded_files
                    ):
                        input_path = (
                            temp_dir
                            / f"{index}_{uploaded_file.name}"
                        )

                        input_path.write_bytes(
                            uploaded_file.getbuffer()
                        )

                        input_paths.append(input_path)

                    output_name = clean_pdf_filename(
                        merge_filename,
                        "merged.pdf",
                    )

                    output_path = (
                        temp_dir
                        / output_name
                    )

                    merge_pdfs(
                        input_paths,
                        output_path,
                    )

                    merged_data = output_path.read_bytes()

                    st.success(
                        "Your PDFs were merged successfully."
                    )

                    st.download_button(
                        label="Download Merged PDF",
                        data=merged_data,
                        file_name=output_name,
                        mime="application/pdf",
                        use_container_width=True,
                    )

            except Exception as exc:
                st.error(
                    f"Unable to merge PDFs: {exc}"
                )


with tab_split:
    st.subheader("Split PDF")

    st.write(
        "Upload one PDF and choose the pages "
        "you want to extract into a new PDF."
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        accept_multiple_files=False,
        key="split_file",
    )

    total_pages = None

    if uploaded_file is not None:
        total_pages = get_pdf_page_count(
            uploaded_file
        )

        if total_pages is not None:
            st.info(
                f"{uploaded_file.name} contains "
                f"{total_pages} page(s)."
            )

    page_selection = st.text_input(
        "Pages to extract",
        placeholder="Example: 1-3,5,7-9",
        key="page_selection",
    )

    st.caption(
        "Examples: 1-3 extracts pages 1 to 3. "
        "1,4,6 extracts individual pages. "
        "1-3,5,7-9 combines both formats."
    )

    split_filename = st.text_input(
        "Extracted file name",
        value="split.pdf",
        key="split_filename",
    )

    if st.button(
        "Extract Pages",
        type="primary",
        key="split_button",
        use_container_width=True,
    ):
        if uploaded_file is None:
            st.error(
                "Please upload a PDF file."
            )

        elif not page_selection.strip():
            st.error(
                "Please enter the pages you want to extract."
            )

        else:
            try:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_dir = Path(temp_dir)

                    input_path = (
                        temp_dir
                        / uploaded_file.name
                    )

                    input_path.write_bytes(
                        uploaded_file.getbuffer()
                    )

                    output_name = clean_pdf_filename(
                        split_filename,
                        "split.pdf",
                    )

                    output_path = (
                        temp_dir
                        / output_name
                    )

                    split_pdf(
                        input_path,
                        page_selection,
                        output_path,
                    )

                    split_data = output_path.read_bytes()

                    st.success(
                        "Selected pages were extracted successfully."
                    )

                    st.download_button(
                        label="Download Extracted PDF",
                        data=split_data,
                        file_name=output_name,
                        mime="application/pdf",
                        use_container_width=True,
                    )

            except Exception as exc:
                st.error(
                    f"Unable to extract pages: {exc}"
                )