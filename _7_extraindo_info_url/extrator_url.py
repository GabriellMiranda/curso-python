class ExtratorURL:
    def __init__(self, url: str) -> None:
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url: str) -> str:
        return url.strip()

    def valida_url(self) -> ValueError:
        if not self.url:
            raise ValueError('url invalida')

    def get_url_base(self) -> str:
        indice_interrogacao = self.url.find("?")
        url_base = self.url[0: indice_interrogacao]
        return url_base

    def get_url_parametros(self) -> None:
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametros(self, parametro_busca: str) -> str:
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __str__(self) -> str:
        return self.url

    def __len__(self) -> int:
        return len(self.url)

if __name__=='__main__':
    extrator_url = ExtratorURL("https/bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")
    valor_quantidade = extrator_url.get_valor_parametros('quantidade')
    print(valor_quantidade)
