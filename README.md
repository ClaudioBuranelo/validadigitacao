# validadigitacao

Biblioteca Python para validação de digitados através da extração de dados via OCR de imagens/PDFs e comparação com JSON fornecido.

## Funcionalidades

- Extração de texto via OCR (pytesseract + Pillow)
- Conversão de PDFs para imagens (pdf2image)
- Extração de campos estruturados via regex
- Comparação detalhada de JSON com deepdiff
- Relatório em JSON com extrações e diferenças
