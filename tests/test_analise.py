import unittest
from validadigitacao.analisador import Analisador

class TestAnalisador(unittest.TestCase):
    def setUp(self):
        self.json_digitado = {
            "nome": "João Silva",
            "cpf": "123.456.789-00",
            "data_nascimento": "01/01/1990"
        }
        self.padroes = {
            "nome": r"Nome:\s*(.+)",
            "cpf": r"CPF:\s*([\d\.\-]+)",
            "data_nascimento": r"Data de nascimento:\s*(\d{2}/\d{2}/\d{4})"
        }
        self.analisador = Analisador(lang_ocr='por', padroes_campos=self.padroes)

    def test_analisar_com_arquivo_invalido(self):
        with self.assertRaises(FileNotFoundError):
            self.analisador.analisar(self.json_digitado, ["arquivo_inexistente.pdf"])

    def test_analisar_com_texto_simulado(self):
        # Para não depender de arquivos reais, vamos testar a extração de campos em um texto mock
        texto_mock = """
        Nome: João Silva
        CPF: 123.456.789-00
        Data de nascimento: 01/01/1990
        """

        campos = self.analisador.extrator.extrair_campos(texto_mock, self.padroes)
        self.assertEqual(campos["nome"], "João Silva")
        self.assertEqual(campos["cpf"], "123.456.789-00")
        self.assertEqual(campos["data_nascimento"], "01/01/1990")

if __name__ == "__main__":
    unittest.main()
