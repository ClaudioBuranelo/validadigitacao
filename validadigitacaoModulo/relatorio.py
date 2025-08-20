import os
import json
from .ocr import extrair_texto_imagem
from .extrator import extract_fields
from .comparador import comparar_dados_extraidos_com_json
from .pdf_converter import converter_pdf_para_imagens


def gerar_relatorio(json_referencia: dict, arquivos: list[str]) -> dict:
    """
    Gera um relatório consolidado a partir de arquivos (PDF/Imagens) e um JSON de referência.
    
    :param json_referencia: JSON com os dados esperados
    :param arquivos: lista de caminhos de arquivos para validar
    :return: dicionário com relatório consolidado
    """
    resultados = []

    for arquivo in arquivos:
        extensao = os.path.splitext(arquivo)[1].lower()

        textos_extraidos = []

        if extensao == ".pdf":
            # 1. Converter PDF para imagens
            imagens = converter_pdf_para_imagens(arquivo)
            # 2. Extrair texto de cada página
            for img in imagens:
                textos_extraidos.append(extrair_texto_imagem(img))
        else:
            # Caso seja imagem direta (png, jpg, etc)
            textos_extraidos.append(extrair_texto_imagem(arquivo))

        # Concatenar todos os textos (se tiver várias páginas do PDF)
        texto_final = "\n".join(textos_extraidos)

        # 3. Extrair campos via regex
        campos_extraidos = extract_fields(texto_final)

        # 4. Comparar com JSON de referência
        diferencas = comparar_dados_extraidos_com_json(json_referencia, campos_extraidos)

        # 5. Montar resultado individual
        resultados.append({
            "arquivo": arquivo,
            "texto_extraido": texto_final,
            "campos_extraidos": campos_extraidos,
            "diferencas": diferencas
        })
    
    # Relatório final
    relatorio = {
        "referencia": json_referencia,
        "resultados": resultados
    }

    return relatorio


def salvar_relatorio(relatorio: dict, caminho_saida: str):
    """
    Salva o relatório em formato JSON.
    """
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)
