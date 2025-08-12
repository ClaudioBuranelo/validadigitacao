from deepdiff import DeepDiff
from typing import Dict, Any

class Comparador:
    def __init__(self):
        pass

    def comparar(self, json_digitado: Dict[str, Any], json_extraido: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compara dois dicionários JSON e retorna um relatório detalhado das diferenças.

        Usa deepdiff para análise profunda.
        """
        diff = DeepDiff(json_digitado, json_extraido, ignore_order=True, report_repetition=True)
        return diff.to_dict()  # Retorna em formato serializável JSON
