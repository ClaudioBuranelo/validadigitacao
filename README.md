# validadigitacao

Biblioteca Python para validação de digitados através da extração de dados via OCR de imagens/PDFs e comparação com JSON fornecido.

## Funcionalidades

- Extração de texto via OCR (pytesseract + Pillow)
- Conversão de PDFs para imagens (pdf2image)
- Extração de campos estruturados via regex
- Comparação detalhada de JSON com deepdiff
- Relatório em JSON com extrações e diferenças

## Requisitos

- Python 3.7+
- Tesseract OCR instalado no sistema (https://github.com/tesseract-ocr/tesseract)
- Poppler para pdf2image instalado (ex: `poppler-utils` no Linux)

## Instalação
pip install -r requirements.txt

## Uso básico
from validadigitacao.analisador import Analisador

json_digitado = {...} # seu JSON
padroes = {...} # regex para extração

analisador = Analisador(lang_ocr="por", padroes_campos=padroes)
resultado = analisador.analisar(json_digitado, ["documento.pdf", "imagem.png"])

print(resultado)

## Rodando testes
python -m unittest discover tests
