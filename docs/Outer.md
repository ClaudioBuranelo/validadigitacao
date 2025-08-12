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

Para desenvolver a biblioteca Python chamada **validadigitacao** com as funcionalidades que você descreveu, aqui está uma proposta inicial de implementação e estrutura para os arquivos principais, considerando as tecnologias sugeridas:

***

## Estrutura do Projeto

```
validadigitacao/
├── validadigitacao/
│   ├── __init__.py
│   ├── extrator.py         # Lê e extrai dados do PDF/imagem via OCR
│   ├── comparador.py       # Compara dados extraídos com JSON recebido
│   └── analisador.py       # Coordena extração, comparação e gera resultado final
├── tests/
│   └── test_analise.py     # Testes unitários básicos
├── README.md
├── requirements.txt
└── setup.py                # Opcional para empacotamento
```

***

## Ideia geral para cada módulo

### 1. extrator.py

- Recebe arquivo(s) PDF ou imagem(s)
- Utiliza `pdf2image` para converter PDFs em imagens (se necessário)
- Usa `pytesseract` e `Pillow` para extrair texto via OCR das imagens
- Retorna os dados extraídos em formato estruturado (exemplo: dicionário Python)

### 2. comparador.py

- Recebe o JSON original (digitado) e os dados extraídos da imagem/PDF
- Compara valores relevantes usando lógica personalizada e/ou bibliotecas como `deepdiff`
- Gera um log detalhado das diferenças e similaridades em JSON

### 3. analisador.py

- Função orquestradora que recebe o JSON e a lista de arquivos
- Chama o extrator para capturar os dados
- Chama o comparador para fazer a comparação
- Gera e retorna o resultado final em JSON, incluindo relatório e texto extraído

***

## Tecnologias a serem usadas

- OCR: `pytesseract`, `Pillow`
- Conversão PDF → imagem: `pdf2image` ou `PyMuPDF`
- Comparação: `deepdiff` para diferenças profundas em JSON ou `difflib` para comparações textuais
- Testes: `unittest` ou `pytest`

***
