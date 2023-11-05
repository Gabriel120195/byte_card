from excecoes import ValorExcedidoException
from datetime import date, datetime
from sqlalchemy import String, Numeric, Date, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db

class Cartao(db.Model):
    __tablename__ = "cartoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(30))
    cvv: Mapped[str] = mapped_column(String(3))
    limite: Mapped[float] = mapped_column(Numeric(precision=15,scale=2))
    validade: Mapped[date] = mapped_column(Date())
    cliente: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(100))

    def __init__(self, **kwargs):
        super().__init__(status='ATIVO', **kwargs)
        
    def cancela(self):
        self.__status = "CANCELADO"

    def ativa(self):
        self.__status = "ATIVO"

    @property
    def is_ativo(self):
        return self.status == "ATIVO"

    @property
    def is_cancelado(self):
        return self.status == "CANCELADO"

    def __str__(self):
        return f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}'

    def __repr__(self) -> str:
        return f'Cartao(id={self.id!r}, numero={self.numero!r},0cvv = {self.cvv!r}, validade = {self.validade!r},limite={self.limite!r}, cliente={self.cliente!r},status={self.status!r})'

    # @property
    # def id(self):
    #     return self.__id

    # @property
    # def numero(self):
    #     return self.__numero

    # @property
    # def validade(self):
    #     return self.__validade

    # @property
    # def cvv(self):
    #     return self.__cvv

    # @property
    # def limite(self):
    #     return self.__limite

    # @limite.setter
    # def limite(self, limite):
    #      self.__set__limite(limite)

    # @property
    # def cliente(self):
    #     return self.__cliente

    # @property
    # def status(self):
    #     return self.__status

    # def __str__(self):
    #     return (f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}')


    # def __set__limite(self, limite):
    #     limite_minimo = 10
        
    #     if limite < limite_minimo:
    #         raise ValueError(f'O limite deve ser de no mínimo {limite_minimo}')
        
    #     self.__limite = limite


    # def __set_cliente(self, cliente):
    #     if not isinstance(cliente, str) or len(cliente.split()) != 2:
    #         raise ValueError("Cliente deve conter exatamente dois nomes separados por espaço.")
            
    #     nomes = cliente.split()
    #     for nome in nomes:
    #         if len(nome) < 2:
    #             raise ValueError("Cada nome deve ter pelo menos dois caracteres.")
            
    #     self.__cliente = cliente



class Compra(db.Model):
    __tablename__ = "compras"

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[float] = mapped_column(Numeric(precision=15, scale=2))
    data: Mapped[datetime] = mapped_column(DateTime())
    estabelecimento: Mapped[str] = mapped_column(String(1000))
    categoria: Mapped[str] = mapped_column(String(255))

    cartao_id: Mapped[int] = mapped_column(ForeignKey("cartoes.id"))
    cartao: Mapped['Cartao'] = relationship()

    def __repr__(self) -> str:
        return f'Compra(id={self.id!r}, valor={self.valor!r},data = {self.data!r}, estabelecimento = {self.estabelecimento!r},categoria = {self.categoria!r}, cartao = {self.cartao!r})'

    def __str__(self):
        return f'Compra: {self.__valor} no dia {self.__data} em {self.__estabelecimento} no cartão {self.__cartao.numero}'

    # @property
    # def valor(self):
    #     return self.__valor

    # @property
    # def categoria(self):
    #     return self.__categoria


    # def __set__estabelecimento(self, estabelecimento):
    #     limite_caracteres = 30
    #     tamanho_estabelecimento = len(estabelecimento)
        
    #     if tamanho_estabelecimento > limite_caracteres:
    #         raise ValueError(f'Estabelecimento com {tamanho_estabelecimento} caracteres é superior ao limite de {limite_caracteres} caracteres')
    
    #     self.__estabelecimento = estabelecimento.strip()


    # def __set__valor(self, valor):
    #     if valor <= 0:
    #         raise ValueError(f"O valor {valor} deve ser superior a zero")
        
    #     self.__valor = valor


    # def __set__cartao(self, cartao):
    #     if cartao is None:
    #         raise ValueError("É obrigatório um cartão")
        
    #     self.__cartao = cartao


    # def valida_compra(self):
    #     limite = self.__cartao.limite
    #     valor = self.__valor
        
    #     if valor > limite:
    #         valor_excedido = valor - limite
    #         raise ValorExcedidoException(f'O valor da compra excedeu ${valor_excedido} do limite') 


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