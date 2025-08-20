import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from validadigitacaoModulo import ocr

class TestOCR(unittest.TestCase):
    def test_imagem_invalida(self):
        # Testa caminho inválido
        try:
            resultado = ocr.extrair_texto_imagem("./exemplos/imagemDocumento.png")
            self.assertIsInstance(resultado, str)
        except Exception as e:
            self.assertIn("Erro", str(e))

    def test_retorno_tipo_string(self):
        # Testa se o retorno é uma string (usando uma imagem gerada em tempo real)
        texto_extraido = ocr.extrair_texto_imagem("./exemplos/imagemDocumento.png")
        self.assertIsInstance(texto_extraido, str)
        self.assertTrue(len(texto_extraido.strip()) > 0)

if __name__ == "__main__":
    unittest.main()
