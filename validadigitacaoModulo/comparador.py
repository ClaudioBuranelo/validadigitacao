from deepdiff import DeepDiff
from validadigitacaoModulo.extrator import extract_fields
from validadigitacaoModulo.ocr import extrair_texto_imagem
from validadigitacaoModulo.pdf_converter import converter_pdf_para_imagens

def comparar_dados_extraidos_com_json(json_referencia, campos_extraidos):
    """
    Compara os dados extraídos de um documento (PDF ou imagem) com os dados esperados em JSON.
    Retorna as diferenças encontradas.
    """

    if isinstance(campos_extraidos, str) and campos_extraidos.startswith("Erro"):
        return campos_extraidos

    #dados_extraidos = extract_fields(campos_extraidos)
    diferencas = DeepDiff(json_referencia, campos_extraidos, ignore_order=True)
    return diferencas
