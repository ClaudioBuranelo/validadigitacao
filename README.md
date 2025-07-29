# 📦 validadigitacao

Uma biblioteca Python para buscar e comparar numeros de documentos e outras informações que foram digitadas, criada para facilitar a conferencia dos dados digitados em projetos dos clientes.

Docstrings no código: Use o padrão PEP 257 para documentar funções, classes e métodos.

Gerar documentação automática: Ferramentas como Sphinx ou MkDocs ajudam a criar sites de documentação a partir do seu código.

## 🚀 Instalação

Você pode instalar diretamente via `pip`:
pip install validadigitacao

git clone https://github.com/seuusuario/NomeDaBiblioteca.git
cd NomeDaBiblioteca
pip install .

## 🧠 Funcionalidades
📄 Leitura de documentos com OCR
🧾 Extração automática de dados estruturados
🔍 Comparação com dados digitados
✅ Geração de relatório com os resultados da comparação
✅ Recebe os dados no formato JSON e a lista de arquivos para buscar a informação
✅ Compara as informações gerando um log no formato JSON
✅ Retorna o texto em formato JSON

## 📚 Exemplo de Uso

from docmatcher import process_document

documento = "caminho/para/documento.pdf"
dados_digitados = {
    "nome": "João da Silva",
    "cpf": "123.456.789-00",
    "data_nascimento": "01/01/1990"
}

resultado = process_document(documento, dados_digitados)

for campo, status in resultado.items():
    print(f"{campo}: {'✔️' if status else '❌'}")


## 🧪 Testes
pytest tests/

## 📄 Licença
Este projeto não mestá licenciado.

🙋‍♂️ Suporte
Para dúvidas, sugestões ou problemas, abra uma issue ou entre em contato pelo e-mail: suporte@brbc.tec.br