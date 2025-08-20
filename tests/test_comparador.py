import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from validadigitacaoModulo import comparador

class TestComparador(unittest.TestCase):

    def test_comparacao_com_dados_corretos(self):
        caminho = "./exemplos/CNH_Joao_da_Silva.pdf"
        dados_esperados = {
            "nome": "João da Silva",
            "cpf": "123.456.789-00"
        }
        resultado = comparador.comparar_dados_extraidos_com_json(caminho, dados_esperados)
        self.assertTrue(isinstance(resultado, dict))  # DeepDiff retorna um dict

    def test_documento_invalido(self):
        caminho = "./exemplos/CNH_Joao_da_Silva.pdf"
        dados_esperados = {}
        resultado = comparador.comparar_dados_extraidos_com_json(caminho, dados_esperados)
        self.assertTrue(isinstance(resultado, str) and "Erro" in resultado)

if __name__ == "__main__":
    unittest.main()
