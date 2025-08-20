import os
import importlib.util

def verificar_imports(caminho_tests='tests', caminho_modulo='validadigitacaoModulo'):
    print("Verificando imports nos arquivos de teste...\n")

    for nome_arquivo in os.listdir(caminho_tests):
        if nome_arquivo.endswith('.py'):
            caminho_completo = os.path.join(caminho_tests, nome_arquivo)
            print(f"Arquivo: {nome_arquivo}")

            try:
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()

                linhas_import = [linha for linha in conteudo.splitlines() if 'validadigitacaoModulo' in linha and 'import' in linha]

                if not linhas_import:
                    print("  ⚠️ Nenhum import relacionado a 'validadigitacaoModulo' encontrado.")
                    continue

                for linha in linhas_import:
                    try:
                        partes = linha.split('import')
                        modulo_nome = partes[1].strip()
                        if modulo_nome.startswith('validadigitacaoModulo.'):
                            modulo_nome = modulo_nome
                        else:
                            modulo_nome = f"validadigitacaoModulo.{modulo_nome}"

                        spec = importlib.util.find_spec(modulo_nome)
                        if spec is None:
                            raise ImportError(f"Módulo '{modulo_nome}' não encontrado.")
                        importlib.import_module(modulo_nome)
                        print(f"  ✅ Import bem-sucedido: {modulo_nome}")
                    except Exception as e:
                        print(f"  ❌ Erro ao importar '{modulo_nome}': {e}")
            except Exception as e:
                print(f"  ❌ Erro ao ler o arquivo '{nome_arquivo}': {e}")
            print()

verificar_imports()
