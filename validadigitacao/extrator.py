import os
import re
from typing import List, Dict, Union
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

class Extrator:
    def __init__(self, lang: str = 'por'):
        """
        lang: código de idioma para o pytesseract (exemplo: 'por' para português)
        """
        self.lang = lang

    def _pdf_para_imagens(self, caminho_pdf: str) -> List[Image.Image]:
        """Converte todas as páginas do PDF em imagens PIL"""
        imagens = convert_from_path(caminho_pdf, dpi=300)
        return imagens

    def _extrair_texto_da_imagem(self, imagem: Image.Image) -> str:
        """Extrai texto OCR de uma imagem PIL"""
        texto = pytesseract.image_to_string(imagem, lang=self.lang)
        return texto

    def extrair_texto(self, caminho_arquivo: str) -> str:
        """Extrai texto de um arquivo PDF ou imagem"""
        extensao = os.path.splitext(caminho_arquivo)[1].lower()
        textos = []
        if extensao == '.pdf':
            imagens = self._pdf_para_imagens(caminho_arquivo)
            for img in imagens:
                textos.append(self._extrair_texto_da_imagem(img))
        elif extensao in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
            img = Image.open(caminho_arquivo)
            textos.append(self._extrair_texto_da_imagem(img))
        else:
            raise ValueError(f"Formato de arquivo não suportado: {extensao}")

        return "\n".join(textos)

    def extrair_campos(self, texto: str, padroes: Dict[str, str]) -> Dict[str, Union[str, None]]:
        """
        Extrai campos definidos por expressões regulares do texto OCR

        padroes: dicionário { nome_campo: regex_para_captura }

        Retorna dict com chave nome_campo e valor texto extraído ou None se não encontrado
        """
        resultado = {}
        for campo, regex in padroes.items():
            match = re.search(regex, texto, re.MULTILINE | re.IGNORECASE)
            if match:
                resultado[campo] = match.group(1).strip()
            else:
                resultado[campo] = None
        return resultado
