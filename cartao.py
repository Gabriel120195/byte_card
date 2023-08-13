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


