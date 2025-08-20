# validadigitacaoModulo/pdf_converter.py
from pdf2image import convert_from_path
import os

def converter_pdf_para_imagens(caminho_pdf, pasta_saida="output", dpi=300):
    try:
        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)

        imagens = convert_from_path(caminho_pdf, dpi=dpi)
        caminhos_imagens = []

        for i, imagem in enumerate(imagens):
            caminho_imagem = os.path.join(pasta_saida, f"pagina_{i+1}.png")
            imagem.save(caminho_imagem, "PNG")
            caminhos_imagens.append(caminho_imagem)

        return caminhos_imagens
    except Exception as e:
        return f"Erro ao converter PDF: {str(e)}"
