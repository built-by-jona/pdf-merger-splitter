"""Branded Streamlit interface for PDF Merger & Splitter."""

from __future__ import annotations

import logging
import tempfile
from pathlib import Path

import streamlit as st
from pypdf import PdfReader

from pdf_tools import merge_pdfs, split_pdf


LOGGER = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent
LOGO_PATH = PROJECT_ROOT / "assets" / "logo.png"

PDF_MIME_TYPE = "application/pdf"

NAVY = "#08275B"
TEAL = "#0A8F78"


# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------


def clean_pdf_filename(filename: str, default_name: str) -> str:
    """Return a valid PDF filename."""
    filename = filename.strip()

    if not filename:
        filename = default_name

    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"

    return filename


def get_pdf_page_count(uploaded_file) -> int | None:
    """Return the number of pages in an uploaded PDF."""
    try:
        uploaded_file.seek(0)
        reader = PdfReader(uploaded_file)
        page_count = len(reader.pages)
        uploaded_file.seek(0)

        return page_count

    except Exception:
        LOGGER.exception("Could not read uploaded PDF page count.")

        try:
            uploaded_file.seek(0)
        except Exception:
            pass

        return None


# ---------------------------------------------------------
# STYLING
# ---------------------------------------------------------


def apply_custom_styles() -> None:
    """Apply the Built by J.O.N.A. navy-and-teal visual theme."""
    st.markdown(
        f"""
        <style>
        :root {{
            --jona-navy: {NAVY};
            --jona-teal: {TEAL};
            --jona-pale-teal: #E9F7F3;
            --jona-border: #D7E0EC;
            --jona-muted: #526681;
        }}

        .stApp {{
            background: #FFFFFF;
            color: var(--jona-navy);
        }}

        [data-testid="stMainBlockContainer"] {{
            max-width: 1400px;
            padding-top: 0.5rem;
            padding-bottom: 1.25rem;
        }}

        h1, h2, h3, h4 {{
            color: var(--jona-navy);
        }}

        .stApp .tool-name {{
            color: var(--jona-navy);
            font-size: clamp(2.1rem, 4vw, 3.65rem) !important;
            font-weight: 800;
            letter-spacing: -0.035em;
            line-height: 1.05;
            margin: 0;
        }}

        .hero-title {{
            align-items: flex-end;
            display: flex;
            min-height: 250px;
            padding-bottom: 0.5rem;
        }}

        .st-key-hero_logo
        [data-testid="stFullScreenFrame"]:has([data-testid="stImage"]) {{
            display: flex;
            justify-content: flex-end;
        }}

        .st-key-hero_logo {{
            align-items: flex-end;
        }}

        .logo-fallback {{
            align-items: center;
            background: var(--jona-pale-teal);
            border: 2px solid var(--jona-teal);
            border-radius: 50%;
            color: var(--jona-navy);
            display: flex;
            font-size: 1.35rem;
            font-weight: 800;
            height: 200px;
            justify-content: center;
            margin: 0 auto;
            text-align: center;
            width: 200px;
        }}

        .navy-divider {{
            background: var(--jona-navy);
            border-radius: 999px;
            height: 10px;
            margin: 0.5rem 0 1.5rem;
            width: 100%;
        }}

        .stApp .intro-copy {{
            color: var(--jona-navy);
            font-size: 1.18rem !important;
            margin: 0 0 1.5rem;
        }}

        .instructions-heading {{
            align-items: center;
            color: var(--jona-navy);
            display: flex;
            font-size: 1.65rem;
            font-weight: 800;
            gap: 0.75rem;
            margin: 0;
        }}

        .instructions-icon,
        .card-icon {{
            align-items: center;
            background: var(--jona-pale-teal);
            border-radius: 50%;
            color: var(--jona-teal);
            display: inline-flex;
            flex: 0 0 auto;
            font-weight: 800;
            justify-content: center;
        }}

        .instructions-icon {{
            font-size: 1.25rem;
            height: 3.15rem;
            width: 3.15rem;
        }}

        .steps-list {{
            counter-reset: steps;
            list-style: none;
            margin: 0.9rem 0 2rem 4.15rem;
            padding: 0;
        }}

        .steps-list li {{
            align-items: center;
            color: var(--jona-navy);
            display: flex;
            font-size: 1.04rem;
            gap: 0.8rem;
            margin: 0.48rem 0;
        }}

        .steps-list li::before {{
            align-items: center;
            background: var(--jona-teal);
            border-radius: 50%;
            color: #FFFFFF;
            content: counter(steps);
            counter-increment: steps;
            display: inline-flex;
            flex: 0 0 1.65rem;
            font-size: 0.88rem;
            font-weight: 700;
            height: 1.65rem;
            justify-content: center;
        }}

        .st-key-tool_card {{
            background: #FFFFFF;
            border: 1px solid var(--jona-border) !important;
            border-radius: 18px !important;
            box-shadow: 0 10px 28px rgba(8, 39, 91, 0.08);
            padding: 0.75rem 0.85rem;
        }}

        .card-heading {{
            align-items: center;
            display: flex;
            gap: 0.8rem;
            margin-bottom: 0.25rem;
        }}

        .card-heading h3 {{
            color: var(--jona-navy);
            font-size: 1.4rem;
            font-weight: 800;
            margin: 0;
        }}

        .card-icon {{
            font-size: 1.35rem;
            height: 3rem;
            width: 3rem;
        }}

        .card-copy {{
            color: var(--jona-navy);
            font-size: 1rem;
            margin: 0.3rem 0 1rem 3.8rem;
        }}

        .file-note {{
            color: var(--jona-muted);
            font-size: 0.9rem;
            margin-top: 0.45rem;
        }}

        [data-testid="stDownloadButton"] button,
        button[kind="primary"] {{
            background: var(--jona-navy);
            border: 1px solid var(--jona-navy);
            border-radius: 10px;
            color: #FFFFFF;
            font-weight: 700;
            min-height: 3rem;
        }}

        [data-testid="stDownloadButton"] button:hover,
        button[kind="primary"]:hover {{
            background: #0D3A7A;
            border-color: #0D3A7A;
            color: #FFFFFF;
        }}

        [data-testid="stFileUploaderDropzone"] {{
            background: #F8FAFD;
            border: 1px dashed #91A3BB;
            border-radius: 12px;
            min-height: 150px;
        }}

        [data-testid="stMetric"] {{
            background: #F8FAFD;
            border: 1px solid var(--jona-border);
            border-radius: 12px;
            padding: 0.9rem 1rem;
        }}

        [data-testid="stMetricLabel"] {{
            color: var(--jona-muted);
        }}

        [data-testid="stMetricValue"] {{
            color: var(--jona-navy);
        }}

        .footer-brand {{
            border-top: 1px solid var(--jona-border);
            color: var(--jona-navy);
            font-size: 0.95rem;
            margin-top: 2.75rem;
            padding: 1.25rem 0 0.4rem;
            text-align: center;
        }}

        .footer-brand strong {{
            font-weight: 800;
        }}

        .footer-brand .footer-accent {{
            color: var(--jona-teal);
        }}

        @media (max-width: 800px) {{
            [data-testid="stMainBlockContainer"] {{
                padding-left: 1.2rem;
                padding-right: 1.2rem;
            }}

            [data-testid="stImage"] {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}

            [data-testid="stFullScreenFrame"]:has([data-testid="stImage"]) {{
                display: flex;
                justify-content: center;
            }}

            .hero-title {{
                justify-content: center;
                min-height: auto;
                text-align: center;
            }}

            .st-key-hero_logo {{
                align-items: center;
                margin-top: 1.25rem;
            }}

            .stApp .tool-name {{
                font-size: clamp(2rem, 10vw, 3rem) !important;
            }}

            .steps-list {{
                margin-left: 0;
            }}

            .steps-list li {{
                align-items: flex-start;
            }}

            .card-copy {{
                margin-left: 0;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# BRAND COMPONENTS
# ---------------------------------------------------------


def show_branded_header() -> None:
    """Display the tool title and Built by J.O.N.A. logo."""
    title_column, logo_column = st.columns(
        [5, 1.5],
        gap="small",
        vertical_alignment="bottom",
    )

    with title_column:
        st.markdown(
            """
            <div class="hero-title">
                <p class="tool-name">PDF Merger &amp; Splitter</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with logo_column:
        st.write("")

        with st.container(key="hero_logo"):
            if LOGO_PATH.is_file():
                try:
                    st.image(str(LOGO_PATH), width=180)
                except Exception:
                    LOGGER.exception("The logo could not be displayed.")
                    show_logo_fallback()
            else:
                show_logo_fallback()


def show_logo_fallback() -> None:
    """Show text branding when the logo cannot be displayed."""
    st.markdown(
        '<div class="logo-fallback">J.O.N.A.</div>',
        unsafe_allow_html=True,
    )


def show_instructions() -> None:
    """Display the PDF Merger & Splitter workflow."""
    st.markdown(
        """
        <div class="instructions-heading">
            <span class="instructions-icon">✓</span>
            <span>How to use this tool</span>
        </div>

        <ol class="steps-list">
            <li>Choose whether you want to merge or split a PDF.</li>
            <li>Upload the PDF file or files you want to process.</li>
            <li>For merging, files are combined in the order shown.</li>
            <li>For splitting, enter the pages you want to extract.</li>
            <li>Download your new PDF when processing is complete.</li>
        </ol>
        """,
        unsafe_allow_html=True,
    )


def show_footer() -> None:
    """Display the Built by J.O.N.A. footer."""
    st.markdown(
        """
        <div class="footer-brand">
            <strong>Built by J.O.N.A.</strong>
            &nbsp;—&nbsp;
            <span class="footer-accent">Just One Next Automation</span>
            &nbsp;—&nbsp;
            <em>Simple tools for complicated work.</em>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# MERGE
# ---------------------------------------------------------


def show_merge_tool() -> None:
    """Display the PDF merge interface."""
    st.markdown(
        """
        <div class="card-heading">
            <span class="card-icon">↑</span>
            <h3>Upload PDFs to merge</h3>
        </div>

        <p class="card-copy">
            Choose two or more PDFs. They will be combined
            in the order shown below.
        </p>
        """,
        unsafe_allow_html=True,
    )

    uploaded_files = st.file_uploader(
        "Choose PDFs to merge",
        type=["pdf"],
        accept_multiple_files=True,
        key="merge_files",
        label_visibility="collapsed",
    )

    st.markdown(
        '<p class="file-note">Supported format: .pdf</p>',
        unsafe_allow_html=True,
    )

    if uploaded_files:
        st.markdown("#### Files to merge")

        for index, uploaded_file in enumerate(
            uploaded_files,
            start=1,
        ):
            page_count = get_pdf_page_count(uploaded_file)

            if page_count is not None:
                st.write(
                    f"**{index}. {uploaded_file.name}** "
                    f"— {page_count} page(s)"
                )
            else:
                st.write(
                    f"**{index}. {uploaded_file.name}**"
                )

    output_name = st.text_input(
        "Merged file name",
        value="merged.pdf",
        key="merge_filename",
    )

    if st.button(
        "Merge PDFs",
        type="primary",
        use_container_width=True,
        key="merge_button",
    ):
        if not uploaded_files or len(uploaded_files) < 2:
            st.warning(
                "Please upload at least two PDF files to merge."
            )
            return

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir = Path(temp_dir)

                input_paths = []

                for index, uploaded_file in enumerate(uploaded_files):
                    input_path = (
                        temp_dir
                        / f"{index}_{uploaded_file.name}"
                    )

                    input_path.write_bytes(
                        uploaded_file.getvalue()
                    )

                    input_paths.append(input_path)

                output_name = clean_pdf_filename(
                    output_name,
                    "merged.pdf",
                )

                output_path = temp_dir / output_name

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
                mime=PDF_MIME_TYPE,
                type="primary",
                icon=":material/download:",
                use_container_width=True,
                key="download_merged_pdf",
            )

        except ValueError as error:
            st.warning(str(error))

        except Exception:
            LOGGER.exception("PDF merge failed.")
            st.error(
                "We could not merge these PDFs. "
                "Please check the files and try again."
            )


# ---------------------------------------------------------
# SPLIT
# ---------------------------------------------------------


def show_split_tool() -> None:
    """Display the PDF split interface."""
    st.markdown(
        """
        <div class="card-heading">
            <span class="card-icon">↑</span>
            <h3>Upload a PDF to split</h3>
        </div>

        <p class="card-copy">
            Choose one PDF and enter the pages you want
            to extract into a new file.
        </p>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Choose PDF to split",
        type=["pdf"],
        accept_multiple_files=False,
        key="split_file",
        label_visibility="collapsed",
    )

    st.markdown(
        '<p class="file-note">Supported format: .pdf</p>',
        unsafe_allow_html=True,
    )

    if uploaded_file is not None:
        page_count = get_pdf_page_count(uploaded_file)

        if page_count is not None:
            metric_columns = st.columns(2)

            metric_columns[0].metric(
                label="File",
                value=uploaded_file.name,
            )

            metric_columns[1].metric(
                label="Total Pages",
                value=page_count,
            )

    page_selection = st.text_input(
        "Pages to extract",
        placeholder="Example: 1-3,5,7-9",
        key="page_selection",
        help=(
            "Use commas for individual pages and hyphens "
            "for page ranges."
        ),
    )

    st.caption(
        "Examples: 1-3 · 1,4,6 · 1-3,5,7-9"
    )

    output_name = st.text_input(
        "Extracted file name",
        value="split.pdf",
        key="split_filename",
    )

    if st.button(
        "Extract Pages",
        type="primary",
        use_container_width=True,
        key="split_button",
    ):
        if uploaded_file is None:
            st.warning(
                "Please upload a PDF file to split."
            )
            return

        if not page_selection.strip():
            st.warning(
                "Please enter the pages you want to extract."
            )
            return

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir = Path(temp_dir)

                input_path = temp_dir / uploaded_file.name

                input_path.write_bytes(
                    uploaded_file.getvalue()
                )

                output_name = clean_pdf_filename(
                    output_name,
                    "split.pdf",
                )

                output_path = temp_dir / output_name

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
                mime=PDF_MIME_TYPE,
                type="primary",
                icon=":material/download:",
                use_container_width=True,
                key="download_split_pdf",
            )

        except ValueError as error:
            st.warning(str(error))

        except Exception:
            LOGGER.exception("PDF split failed.")
            st.error(
                "We could not split this PDF. "
                "Please check the file and page selection "
                "and try again."
            )


# ---------------------------------------------------------
# MAIN APP
# ---------------------------------------------------------


def main() -> None:
    """Render the PDF Merger & Splitter Streamlit application."""
    st.set_page_config(
        page_title="PDF Merger & Splitter",
        page_icon="📄",
        layout="wide",
    )

    apply_custom_styles()
    show_branded_header()

    st.markdown(
        '<div class="navy-divider"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="intro-copy">
            Combine multiple PDF files into one document
            or extract only the pages you need.
        </p>
        """,
        unsafe_allow_html=True,
    )

    show_instructions()

    with st.container(
        border=True,
        key="tool_card",
    ):
        merge_tab, split_tab = st.tabs(
            [
                "Merge PDFs",
                "Split PDF",
            ]
        )

        with merge_tab:
            show_merge_tool()

        with split_tab:
            show_split_tool()

    show_footer()


if __name__ == "__main__":
    main()