import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validadigitacaoModulo.relatorio import gerar_relatorio, salvar_relatorio

json_referencia = {
    "nome": "João da Silva",
    "cpf": "123.456.789-00",
    "data_nascimento": "01/01/1990",
    "nome_mae": "Maria da Silva"
}

arquivos = [
    "./exemplos/CNH_Joao_da_Silva.pdf",
    "./exemplos/imagemDocumento.png"
]

relatorio = gerar_relatorio(json_referencia, arquivos)
salvar_relatorio(relatorio, "./exemplos/saida/relatorio.json")
