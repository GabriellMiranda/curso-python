import requests
class SearchAdress:

    def __init__(self, cep: str) -> None:
        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError("Cep invalid")


    def cep_is_valid(self, cep: str) -> bool:
        if len(cep) == 8:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return f'{self.cep[:5]}-{self.cep[5:]}'


    def acess_by_cep(self) -> dict:
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )


if __name__=='__main__':
    cep = '01001000'
    obj_cep = SearchAdress(cep)
    print(obj_cep.acess_by_cep())
    
