
import streamlit as st
import PyPDF2
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(page_title="PDF Merger", layout="wide")
st.title("📄 PDF Merger")

st.text("Hello!☺️")
st.text("This webapp can be used to merge PDFs, you can even select a range of pages you wish to use within each document.")
st.text("Just upload all the documents you wish to merge in order from first to last")

if 'pdfs' not in st.session_state:
    st.session_state.pdfs = []

def parse_page_selection(selection, max_pages):
    """Parse page selection string into list of page numbers"""
    pages = set()

    try:
        parts = selection.split(',')
        for part in parts:
            part = part.strip()
            if '-' in part:
                start, end = part.split('-')
                start, end = int(start), int(end)
                if start < 1 or end > max_pages:
                    return None
                pages.update(range(start, end + 1))
            else:
                page = int(part)
                if page < 1 or page > max_pages:
                    return None
                pages.add(page)

        return sorted(list(pages))
    except:
        return None

# File uploader
uploaded_files = st.file_uploader(
    "Upload PDF files to merge",
    type=['pdf'],
    accept_multiple_files=True,
    key='pdf_uploader'
)

# Process uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        # Check if this file is already in session state
        if not any(pdf['name'] == uploaded_file.name for pdf in st.session_state.pdfs):
            pdf_bytes = uploaded_file.read()
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))

            st.session_state.pdfs.append({
                'name': uploaded_file.name,
                'bytes': pdf_bytes,
                'num_pages': len(pdf_reader.pages),
                'selected_pages': f"1-{len(pdf_reader.pages)}"
            })

# Display uploaded PDFs with preview and page selection
if st.session_state.pdfs:
    st.subheader("Uploaded PDFs")

    for idx, pdf_info in enumerate(st.session_state.pdfs):
        with st.expander(f"📄 {pdf_info['name']} ({pdf_info['num_pages']} pages)", expanded=True):
            col1, col2 = st.columns([2, 1])

            with col1:
                # Page selection input
                st.write("**Select pages to include:**")
                st.caption("Examples: '1,3,5' or '1-5' or '1-3,7,9-12'")

                selected = st.text_input(
                    "Pages",
                    value=pdf_info['selected_pages'],
                    key=f"pages_{idx}",
                    label_visibility="collapsed"
                )
                st.session_state.pdfs[idx]['selected_pages'] = selected

                # Remove button
                if st.button(f"Remove this PDF", key=f"remove_{idx}"):
                    st.session_state.pdfs.pop(idx)
                    st.rerun()

            with col2:
                # Preview first page using PyMuPDF
                try:
                    pdf_document = fitz.open(stream=pdf_info['bytes'], filetype="pdf")
                    first_page = pdf_document[0]

                    # Render page to image
                    pix = first_page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
                    img_bytes = pix.tobytes("png")
                    img = Image.open(io.BytesIO(img_bytes))

                    st.image(img, caption="First page preview", use_container_width=True)
                    pdf_document.close()
                except Exception as e:
                    st.warning(f"Could not generate preview: {str(e)}")

    # Merge button
    st.divider()
    if st.button("🔗 Merge PDFs", type="primary", use_container_width=True):
        try:
            merger = PyPDF2.PdfMerger()

            for pdf_info in st.session_state.pdfs:
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_info['bytes']))
                pages = parse_page_selection(pdf_info['selected_pages'], pdf_info['num_pages'])

                if not pages:
                    st.error(f"Invalid page selection for {pdf_info['name']}")
                    continue

                # Add selected pages
                for page_num in pages:
                    merger.append(
                        io.BytesIO(pdf_info['bytes']),
                        pages=(page_num - 1, page_num)
                    )

            # Create merged PDF
            output = io.BytesIO()
            merger.write(output)
            merger.close()
            output.seek(0)

            # Download button
            st.success("✅ PDFs merged successfully!")
            st.download_button(
                label="⬇️ Download Merged PDF",
                data=output.getvalue(),
                file_name="merged_document.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error merging PDFs: {str(e)}")

    # Clear all button
    if st.button("Clear All PDFs"):
        st.session_state.pdfs = []
        st.rerun()

else:
    st.info("👆 Upload PDF files to get started")
