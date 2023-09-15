from random import randint
from datetime import date
from dateutil.relativedelta import relativedelta
import re
class Cartao:
    def __init__(self, numero, validade, cvv, limite, cliente, id = None):
        self.__numero = numero
        self.__validade = validade
        self.__cvv = cvv
        self.__limite = limite
        self.__cliente = cliente
        self.__status = "ATIVO"
        self.__id = id

        
    def cancelar(self):
        self.__status = "CANCELADO"

    def ativar(self):
        self.__status = "ATIVO"

    @property
    def id(self):
        return self.__id

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
    def limite(self, limite):
         self.__limite = limite

    @property
    def cliente(self):
        return self.__cliente

    @property
    def status(self):
        return self.__status

    def __str__(self):
        return (f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}')


class Compra:
    def __init__(self, valor, data, estabelecimento, categoria, cartao, id = None):
        self.__valor = valor 
        self.__data = data 
        self.__estabelecimento = estabelecimento.strip() 
        self.__categoria = categoria.strip()
        self.__cartao = cartao
        self.__id = id

        if len(self.__estabelecimento) > 10:
            print(f'Nome do estabelecimento grande: {self.__estabelecimento}') 

        dia_da_compra = self.__data.strftime('%d/%m/%Y')
        hora_da_compra = self.__data.strftime('%H:%M:%S')
        print(f'Compra realizada no dia {dia_da_compra} na hora {hora_da_compra}')

    def __str__(self):
        return f'Compra: {self.__valor} no dia {self.__data} em {self.__estabelecimento} no cartão {self.__cartao.numero}'

    @property
    def valor(self):
        return self.__valor

    @property
    def categoria(self):
        return self.__categoria


class CompraCredito(Compra):
    def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas = 1, id = None):
        super().__init__(valor, data, estabelecimento, categoria, cartao, id)
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

def cria_numero_cartao():
    grupos_de_numeros = [f'{randint(1, 9999):04}' for i in range(4)]
    return ' '.join(grupos_de_numeros)

def cria_cvv_do_cartao():
    cvv = f'{randint(1, 999):03}'
    return cvv

def define_validade_do_cartao():
    validade = date.today() + relativedelta(years=4, months=6, day=31)
    return validade















