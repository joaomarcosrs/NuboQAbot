from pdfminer.high_level import extract_text


def extract_text_from_pdf(file_path: str) -> str:
    return extract_text(file_path)