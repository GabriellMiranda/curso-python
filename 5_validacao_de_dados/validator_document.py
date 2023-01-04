from validate_docbr import CPF, CNPJ

#Factory method
class Document:

    @staticmethod
    def creat_document(document):
        if(len(document)==11):
            return Cpf(document)
        elif (len(document) == 14):
            return Cnpj(document)
        else:
            raise ValueError("error")

class Cpf:
    def __init__(self,document:str) -> None:
        if self.cpf_validate(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!!")

    @staticmethod
    def cpf_validate(document:str):
            return CPF().validate(document)
    
    def __str__(self) -> str:
        return CPF().mask(self.cpf)

    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return f"{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}"


class Cnpj:
    def __init__(self, document:str) -> None:
        if self.cnpj_validate(document):
            self.document = document
            self.cnpj = CNPJ()
        else:
            raise ValueError("CNPJ invalid")
        
    def cnpj_validate(self) -> bool:
        is_valid = self.cnpj.validate(self.document)
        if not is_valid:
            raise ValueError("CNPJ invalid")
        return True
        

    def __str__(self) -> str:
        return self.cnpj.generate(self.cnpj)