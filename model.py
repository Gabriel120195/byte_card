class Cartao:
    def __init__(self, numero, validade, cvv, limite, cliente):
        self.__numero = numero
        self.__validade = validade
        self.__cvv = cvv
        self.__limite = limite
        self.__cliente = cliente
        self.__status = "ATIVO"

    def cancelar(self):
        self.__status = "CANCELADO"

    def ativar(self):
        self.__status = "ATIVO"

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def cvv(self):
        return self.__cvv

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
         self.__limite = novo_limite

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status


class Compra:
    def __init__(self, valor, data, estabelecimento, categoria, cartao):
        self.__valor = valor 
        self.__data = data 
        self.__estabelecimento = estabelecimento 
        self.__categoria = categoria 
        self.__cartao = cartao 

    def __str__(self):
        return f'Compra: {self.__valor}no dia {self.__data} em {self.__estabelecimento} no cartão {self.__cartao.numero}'

    @property
    def valor(self):
        return self.__valor


class CompraCredito(Compra):
    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas):
        super().__init__(valor, data, estabelecimento, categoria, cartao)
        self.__quantidade_parcelas = quantidade_parcelas 

    @property 
    def valor(self): 
        return super().valor * 1.1 

    @property 
    def quantidade_parcelas(self): 
        return self.__quantidade_parcelas 

    @property
    def valor_parcela(self):
        return self.valor / self.quantidade_parcelas 

