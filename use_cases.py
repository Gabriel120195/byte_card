from datetime import date, datetime
from random import randint
from model import Cartao, Compra
from dateutil.relativedelta import relativedelta
from sqlalchemy import select
from database import db

def cria_numero_do_cartao():
    grupos_de_numeros = [f'{randint(1, 9999):04}' for i in range(4)]
    return ' '.join(grupos_de_numeros)

def cria_cvv_do_cartao():
    cvv = f'{randint(1, 999):03}'
    return cvv

def define_validade_do_cartao():
    validade = date.today() + relativedelta(years=4, months=6, day=31)
    return validade

def lista_cartoes():
    comando = select(Cartao).order_by(Cartao.cliente, Cartao.numero)
    resultado = db.session.scalars(comando)

    return list(resultado)

def pesquisa_cartao_por_id(cartao_id):
    return db.session.get(Cartao, cartao_id)

def cadastra_cartao(cliente, limite):
    numero = cria_numero_do_cartao()
    cvv = cria_cvv_do_cartao()
    validade = define_validade_do_cartao()

    cartao = Cartao(numero=numero, validade=validade, cvv=cvv, limite=limite, cliente=cliente)

    db.session.add(cartao)
    db.session.commit()

def cadastra_compra(cartao_id, valor, categoria, estabelecimento):
    cartao = pesquisa_cartao_por_id(cartao_id)
    if not cartao:
        raise ValueError('Cartão não encontrado')

    agora = datetime.now()
    compra = Compra(valor=valor, categoria=categoria, estabelecimento=estabelecimento, cartao=cartao, data=agora)

    db.session.add(compra)
    db.session.commit()

# def lista_compras():
#     return banco_compras
#
# def monta_relatorio_gastos_por_categoria():
#     gasto_por_categoria = defaultdict(float)
#     for compra in lista_compras():
#         gasto_por_categoria[compra.categoria] += compra.valor
#
#     return gasto_por_categoria

def define_limite(cartao_id, limite):
    cartao = pesquisa_cartao_por_id(cartao_id)
    cartao.limite = limite
    db.session.commit()

def altera_status_cartao(cartao_id, operacao):
    cartao = pesquisa_cartao_por_id(cartao_id)
    operacao(cartao)
    db.session.commit()

def ativa_cartao(cartao_id):
    altera_status_cartao(cartao_id, lambda c: c.ativa())

def cancela_cartao(cartao_id):
    altera_status_cartao(cartao_id, lambda c: c.cancela())