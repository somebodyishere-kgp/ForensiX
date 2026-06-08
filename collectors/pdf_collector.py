from PyPDF2 import PdfReader

def get_pdf_metadata(file_path):
    
    pdf = PdfReader(file_path)

    metadata = {}

    if pdf.metadata:
        for k, v in pdf.metadata.items():
            metadata[f"PDF_{k}"] = str(v)

    metadata["PDF_PageCount"] = len(pdf.pages)

    return metadata