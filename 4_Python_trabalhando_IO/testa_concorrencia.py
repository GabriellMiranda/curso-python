arquivo1 = open('/home/gabriel/Documentos/Alura/Python/curso-python/4_Python_trabalhando_IO/dados/contatos.csv', encoding='latin_1', mode='w')
arquivo2 = open('/home/gabriel/Documentos/Alura/Python/curso-python/4_Python_trabalhando_IO/dados/contatos.csv', encoding='latin_1', mode='w')

contato_carol = '11,Carol,carol@gmail.com\n'
contato_adreza = '12,Andreza,Andreza@gmail.com\n'

with open('/home/gabriel/Documentos/Alura/Python/curso-python/4_Python_trabalhando_IO/dados/contatos.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('/home/gabriel/Documentos/Alura/Python/curso-python/4_Python_trabalhando_IO/dados/contatos.csv', encoding='latin_1', mode='w') as arquivo2:
    arquivo2.write(contato_adreza)



arquivo1.write(contato_carol)
arquivo2.write(contato_adreza)

