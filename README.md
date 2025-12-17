# 📄 PDF Merger with Page Selection

A simple and intuitive Streamlit web app that allows you to merge multiple PDF files with the ability to select specific pages or page ranges from each document.

## ✨ Features

- **Multiple PDF Upload**: Upload multiple PDF files at once
- **Live Preview**: See a preview of the first page of each uploaded PDF
- **Flexible Page Selection**: Choose specific pages or ranges using simple syntax
  - Single pages: `1,3,5`
  - Ranges: `1-5`
  - Combined: `1-3,7,9-12`
- **Easy Management**: Remove individual PDFs before merging
- **One-Click Download**: Download your merged PDF with a single click
- **Clean Interface**: User-friendly design with clear instructions

## 🚀 Demo

https://pdfmerger-cjfdata.streamlit.app/

## 📋 Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- PyMuPDF (fitz)
- Pillow

## 🛠️ Installation

### Local Installation

1. Clone this repository:
```bash
git clone https://github.com/CJFData/PDFMerger.git
cd pdf-merger
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run pdf_merger_app.py
```

4. Open your browser and navigate to `http://localhost:8501`

### Jupyter Notebook

If you prefer to run this from a Jupyter notebook, see the included notebook cells in the documentation.

## 📖 Usage

1. **Upload PDFs**: Click the upload button and select one or more PDF files
2. **Preview**: View the first page of each uploaded PDF
3. **Select Pages**: Specify which pages to include from each PDF
   - Default: All pages (e.g., `1-5` for a 5-page document)
   - Custom: Enter your selection (e.g., `1,3,5` or `2-4,7`)
4. **Remove (Optional)**: Remove any PDFs you don't want to include
5. **Merge**: Click the "Merge PDFs" button
6. **Download**: Download your merged PDF file

## 🎨 Example Use Cases

- Combine chapters from different documents
- Extract and merge specific pages from multiple reports
- Create a custom document from various sources
- Merge selected pages from scanned documents

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0) - see the [LICENSE](LICENSE) file for details.

## 👏 Credits

Created with assistance from Claude (Anthropic)

## 📧 Contact

Your Name - [Christian J Ferreira](https://www.linkedin.com/in/christianjferreira/) - data@christianjferreira.com

Project Link: [https://github.com/CJFData/PDFMerger](https://github.com/CJFData/PDFMerger)

---

⭐ If you found this helpful, please consider giving it a star!
