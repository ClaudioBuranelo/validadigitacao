import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from pdf2image import convert_from_path
import re
from PIL import Image

def extract_text_from_image(image_path):
    """Extrai texto de uma imagem usando OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='por')
    return text

def extract_text_from_pdf(pdf_path):
    """Extrai texto de um PDF convertendo páginas em imagens e aplicando OCR."""
    images = convert_from_path(pdf_path)
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image, lang='por')
        full_text += text + "\n"
    return full_text

def extract_fields(text):
    """Extrai campos estruturados como CPF, CNPJ, datas e valores usando regex."""
    cpf_pattern = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
    cnpj_pattern = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b'
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    value_pattern = r'R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}'
    name_pattern = r'\b([A-ZÀ-Ÿ][a-zà-ÿ]+(?:[-\'\s][A-ZÀ-Ÿ][a-zà-ÿ]+)*(?:\s(?:da|de|do|das|dos))?(?:\s[A-ZÀ-Ÿ][a-zà-ÿ]+(?:[-\'\s][A-ZÀ-Ÿ][a-zà-ÿ]+)*)+)\b'

    cpfs = re.findall(cpf_pattern, text)
    cnpjs = re.findall(cnpj_pattern, text)
    dates = re.findall(date_pattern, text)
    values = re.findall(value_pattern, text)
    names = re.findall(name_pattern, text)

    return {
        'cpfs': cpfs,
        'cnpjs': cnpjs,
        'dates': dates,
        'values': values,
        'names': names
    }
