from setuptools import setup, find_packages

setup(
    name="validadigitacao",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytesseract",
        "Pillow",
        "pdf2image",
        "deepdiff"
    ],
    author="Claudio Buranelo",
    description="Biblioteca para validação de digitados via OCR e comparação com JSON",
)
