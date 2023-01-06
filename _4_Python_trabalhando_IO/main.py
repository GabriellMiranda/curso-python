try:
    with open('/home/gabriel/Documentos/Alura/Python/curso-python/4_Python_trabalhando_IO/dados/ontatos.csv', encoding='latin_1') as arquivos:
        conteudo = arquivos.readlines()
        for linha in conteudo:
            print(linha, end='')
except FileNotFoundError as errorFile:
    print(errorFile)
except PermissionError:
    print('Sem permissão de escrita')
