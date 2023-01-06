arquivo_contatos = open('/home/gabriel/Documentos/Alura/Python/curso-python/4_Python_trabalhando_IO/dados/contatos.csv', encoding='latin_1', mode='w+')

contatos = ['11,carol,carol@gmail.com.br\n',
            '12,gabriel,gabriel@gmail.com.br\n',
            '13,Ana,ana@gmail.com.br\n',
            '14,sapiens,sapiens@gmail.com.br\n']
            
for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()

arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)

input("pressione <Enter> para encerar o programa")