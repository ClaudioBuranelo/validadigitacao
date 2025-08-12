import os
import json
from typing import List, Dict, Union
from .extrator import Extrator
from .comparador import Comparador

class Analisador:
    def __init__(self, lang_ocr: str = 'por', padroes_campos: Dict[str, str] = None):
        """
        lang_ocr: idioma para OCR pytesseract
        padroes_campos: dicionário para extração de campos {campo: regex}
        """
        self.extrator = Extrator(lang=lang_ocr)
        self.comparador = Comparador()
        self.padroes_campos = padroes_campos or {}

    def analisar(self, json_digitado: Dict[str, Any], lista_arquivos: List[str]) -> Dict[str, Any]:
        """
        Recebe JSON digitado e lista de arquivos (pdf/imagem),
        executa extração, comparação e retorna resultado final.
        """
        extracoes = []
        textos_extraidos = []

        for arquivo in lista_arquivos:
            if not os.path.exists(arquivo):
                raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

            texto = self.extrator.extrair_texto(arquivo)
            textos_extraidos.append({"arquivo": arquivo, "texto": texto})

            campos_extraidos = self.extrator.extrair_campos(texto, self.padroes_campos)
            extracoes.append({"arquivo": arquivo, "campos": campos_extraidos})

        # Podemos consolidar todas extrações numa estrutura única para comparação:
        json_extraido_combinado = {}
        for extracao in extracoes:
            json_extraido_combinado.update(extracao['campos'])

        diff = self.comparador.comparar(json_digitado, json_extraido_combinado)

        resultado = {
            "comparacao": diff,
            "extracoes": extracoes,
            "textos_extraidos": textos_extraidos
        }

        return resultado
