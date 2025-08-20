"""
validadigitacao - Biblioteca para validação de digitados via OCR e comparação com JSON.

Funcionalidades:
- Extração de texto via OCR (pytesseract + Pillow)
- Conversão de PDFs para imagens (pdf2image)
- Extração de campos estruturados via regex
- Comparação detalhada de JSON com deepdiff
- Geração de relatório em JSON
"""

from .ocr import extrair_texto_imagem
from .extrator import extract_fields
from .pdf_converter import converter_pdf_para_imagens
from .comparador import comparar_dados_extraidos_com_json
#from .relatorio import gerar_relatorio

__all__ = [
  "extrair_texto_imagem",
  "extract_fields",
  "converter_pdf_para_imagens"
  "comparar_dados_extraidos_com_json",
#   "gerar_relatorio"
]
