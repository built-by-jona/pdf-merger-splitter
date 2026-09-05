import tempfile
from pathlib import Path

import streamlit as st

from pdf_tools import merge_pdfs, split_pdf


st.set_page_config(
    page_title="PDF Merger & Splitter",
    page_icon="📄",
    layout="centered",
)


st.title("PDF Merger & Splitter")
st.caption("Merge multiple PDF files or extract selected pages from a PDF.")


tab_merge, tab_split = st.tabs(["Merge PDFs", "Split PDF"])


with tab_merge:
    st.subheader("Merge PDFs")

    uploaded_files = st.file_uploader(
        "Upload at least two PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        key="merge_files",
    )

    if uploaded_files:
        st.write(f"{len(uploaded_files)} file(s) selected")

        for index, uploaded_file in enumerate(uploaded_files, start=1):
            st.write(f"{index}. {uploaded_file.name}")

    merge_filename = st.text_input(
        "Output filename",
        value="merged.pdf",
        key="merge_filename",
    )

    if st.button(
        "Merge PDFs",
        type="primary",
        key="merge_button",
    ):
        if not uploaded_files or len(uploaded_files) < 2:
            st.error("Please upload at least two PDF files.")

        else:
            try:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_dir = Path(temp_dir)

                    input_paths = []

                    for index, uploaded_file in enumerate(uploaded_files):
                        input_path = (
                            temp_dir
                            / f"{index}_{uploaded_file.name}"
                        )

                        input_path.write_bytes(uploaded_file.getbuffer())
                        input_paths.append(input_path)

                    output_name = merge_filename.strip()

                    if not output_name:
                        output_name = "merged.pdf"

                    if not output_name.lower().endswith(".pdf"):
                        output_name += ".pdf"

                    output_path = temp_dir / output_name

                    merge_pdfs(
                        input_paths,
                        output_path,
                    )

                    merged_data = output_path.read_bytes()

                    st.success("PDFs merged successfully.")

                    st.download_button(
                        label="Download Merged PDF",
                        data=merged_data,
                        file_name=output_name,
                        mime="application/pdf",
                    )

            except Exception as exc:
                st.error(str(exc))


with tab_split:
    st.subheader("Split PDF")

    uploaded_file = st.file_uploader(
        "Upload one PDF file",
        type=["pdf"],
        accept_multiple_files=False,
        key="split_file",
    )

    page_selection = st.text_input(
        "Pages to extract",
        placeholder="Example: 1-3,5,7-9",
        key="page_selection",
    )

    st.caption(
        "Use commas for individual pages and hyphens for ranges."
    )

    split_filename = st.text_input(
        "Output filename",
        value="split.pdf",
        key="split_filename",
    )

    if st.button(
        "Extract Pages",
        type="primary",
        key="split_button",
    ):
        if uploaded_file is None:
            st.error("Please upload a PDF file.")

        elif not page_selection.strip():
            st.error("Please enter the pages you want to extract.")

        else:
            try:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_dir = Path(temp_dir)

                    input_path = temp_dir / uploaded_file.name
                    input_path.write_bytes(uploaded_file.getbuffer())

                    output_name = split_filename.strip()

                    if not output_name:
                        output_name = "split.pdf"

                    if not output_name.lower().endswith(".pdf"):
                        output_name += ".pdf"

                    output_path = temp_dir / output_name

                    split_pdf(
                        input_path,
                        page_selection,
                        output_path,
                    )

                    split_data = output_path.read_bytes()

                    st.success("Pages extracted successfully.")

                    st.download_button(
                        label="Download Split PDF",
                        data=split_data,
                        file_name=output_name,
                        mime="application/pdf",
                    )

            except Exception as exc:
                st.error(str(exc))