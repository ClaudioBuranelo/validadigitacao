# 📦 validadigitacao

O Objetivo principal do projeto é receber um objeto do tipo json e um documento que pode ser imagem ou pdf, extrair alguns dados da imagem ou pdf e comparar com o json recebido, retornando um json com a análise.

## 🧠 Funcionalidades
📄 Leitura de documentos com OCR
🧾 Extração automática de dados estruturados
🔍 Comparação com dados digitados
✅ Geração de relatório com os resultados da comparação
✅ Recebe os dados no formato JSON e a lista de arquivos para buscar a informação
✅ Compara as informações gerando um log no formato JSON
✅ Retorna o texto em formato JSON

🗂️ Estrutura sugerida do projeto
validadigitacao/
├── validadigitacao/
│   ├── __init__.py
│   ├── extrator.py         # Lê e extrai dados do PDF/imagem
│   ├── comparador.py       # Compara os dados extraídos com o JSON
│   └── analisador.py       # Orquestra a análise e retorna o JSON final
├── tests/
│   └── test_analise.py     # Testes unitários
├── README.md
├── requirements.txt
└── setup.py                # (opcional, se quiser empacotar)

🧠 Tecnologias que podemos usar
OCR: pytesseract + Pillow para imagens
PDF: pdf2image ou PyMuPDF
Comparação de dados: lógica personalizada com json e difflib (ou deepdiff)


