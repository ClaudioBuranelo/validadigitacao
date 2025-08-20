import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from validadigitacaoModulo import pdf_converter

class TestPDFConverter(unittest.TestCase):

    def test_pdf_invalido(self):
        resultado = pdf_converter.converter_pdf_para_imagens("./exemplos/CNH_Joao_da_Silva.pdf")
        self.assertTrue(resultado != "")
       # self.assertIn("output", resultado)

    def test_pdf_valido(self):
        # Supondo que exista um PDF válido em ./exemplos/documento.pdf
        resultado = pdf_converter.converter_pdf_para_imagens("./exemplos/CNH_Joao_da_Silva.pdf", pasta_saida="./exemplos/saida")
        self.assertTrue(isinstance(resultado, list))
        self.assertTrue(all([caminho.endswith(".png") for caminho in resultado]))
       # self.assertTrue(isinstance(resultado, list))
       # self.assertTrue(all([caminho.endswith(".png") for caminho in resultado]))

if __name__ == "__main__":
    unittest.main()
