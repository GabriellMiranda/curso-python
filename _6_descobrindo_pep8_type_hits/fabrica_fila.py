from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

from constants import TIPO_FILA_NORMAL, TIPOS_FILA_PRIORITARIA

class FabricaFila:

    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaPrioritaria, FilaNormal]:
        tipo_fila = tipo_fila.lower()
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPOS_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe')