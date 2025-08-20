import pytest
from validadigitacaoModulo import extrator


@pytest.fixture
def sample_text():
    return """
    Nome: João da Silva
    CPF: 123.456.789-00
    CNPJ: 12.345.678/0001-99
    Data de emissão: 01/01/2023
    Valor: R$ 1.234,56
    """

def test_extract_fields(sample_text):
    fields = extrator.extract_fields(sample_text)
    assert fields['cpfs'] == ['123.456.789-00']
    assert fields['cnpjs'] == ['12.345.678/0001-99']
    assert fields['dates'] == ['01/01/2023']
    assert fields['values'] == ['R$ 1.234,56']

def test_extract_fields_empty():
    empty_text = "Este texto não contém dados estruturados."
    fields = extrator.extract_fields(empty_text)
    assert fields['cpfs'] == []
    assert fields['cnpjs'] == []
    assert fields['dates'] == []
    assert fields['values'] == []
