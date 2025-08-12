import json
from validadigitacao.analisador import Analisador

# JSON digitado fornecido pelo usuário
json_digitado = {
    "nome": "João Silva",
    "cpf": "123.456.789-00",
    "data_nascimento": "01/01/1990"
}

# Padrões regex para captura de textos estruturados no OCR:
padroes = {
    "nome": r"Nome:\s*(.+)",
    "cpf": r"CPF:\s*([\d\.\-]+)",
    "data_nascimento": r"Data de nascimento:\s*(\d{2}/\d{2}/\d{4})"
}

analisador = Analisador(lang_ocr='por', padroes_campos=padroes)

arquivos = ["documento1.pdf", "foto_rg.png"]

resultado = analisador.analisar(json_digitado, arquivos)

# Resultado é um dict que pode ser salvo ou exibido
print(json.dumps(resultado, indent=2, ensure_ascii=False))
