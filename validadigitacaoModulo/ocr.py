from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import os

def extrair_texto_imagem(caminho_imagem: str) -> str:
    """
    Recebe o caminho de uma imagem e retorna o texto extraído via OCR.
    Utiliza pytesseract com suporte ao idioma português.
    """
    try:
        if not os.path.exists(caminho_imagem):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_imagem}")
        
        imagem = Image.open(caminho_imagem)
        texto = pytesseract.image_to_string(imagem, lang='por')
        return texto.strip()
    
    except Exception as e:
        return f"Erro ao extrair texto da imagem: {str(e)}"
