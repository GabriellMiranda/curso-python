from fabrica_fila import FabricaFila

teste_fabrica = FabricaFila.pega_fila('NorMal')

teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()

print(teste_fabrica.chama_cliente(10))

i = 0
while(True):
    i+=1
    print(i)
