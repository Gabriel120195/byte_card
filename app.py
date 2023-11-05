from flask import Flask, redirect, render_template, request, flash
import forms
import use_cases
from database import db

app = Flask(__name__)

app.secret_key = b'd3fcbe64-7150-11ee-b1fe-93b6661203c1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost:3306/byte_card'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

@app.route('/')
def index():
    return redirect('/cartoes/lista') 

@app.route('/cartoes/lista') 
def lista_cartoes():
    return render_template('cartao/lista.html', cartoes=use_cases.lista_cartoes()) 

@app.route('/cartoes/formulario') 
def formulario_cartao():
    return render_template('cartao/formulario.html') 

@app.route('/cartoes/cadastrar', methods=['POST']) 
def cadastra_cartao():
    form = forms.CadastraCartaoForm(request.form)

    if form.validate():
        use_cases.cadastra_cartao(form.cliente.data, form.limite.data)
        flash("Cartão cadastrado com sucesso.", "info")
        return redirect('/cartoes/lista')

    return formulario_cartao(form)

@app.route('/compras/formulario') 
def formulario_compra(form=None):
    cartoes = use_cases.lista_cartoes()
    return render_template('compra/formulario.html', cartoes=cartoes, form=form)

@app.route('/compras/cadastrar', methods=['POST']) 
def cadastra_compra():
    form = forms.CadastraCompraForm(request.form)
    if form.validate():
        use_cases.cadastra_compra(
            form.cartao.data,
            form.valor.data,
            form.categoria.data,
            form.estabelecimento.data
        )

        flash("Compra cadastrada com sucesso.", "info")

        return redirect('/compras/cadastrar')

    return formulario_compra(form)

@app.route('/cartoes/<id>/cancelar') 
def cancela_cartao(id):
    use_cases.cancela_cartao(id)

    return redirect('/cartoes/lista') 

@app.route('/cartoes/<id>/ativar') 
def ativa_cartao(id):
    cartao_id = int(id)
    use_cases.ativa_cartao(cartao_id)

    return redirect('/cartoes/lista') 

@app.route('/cartoes/<id>/limite') 
def formulario_limite(id, form=None):
    cartao = use_cases.pesquisa_cartao_por_id(id)

    return render_template('cartao/limite.html', cartao=cartao, form=form)

@app.route('/cartoes/alterar-limite', methods=['POST']) 
def altera_limite():
    form = forms.AlteraLimiteForm(request.form)
    if form.validate():
        use_cases.define_limite(form.id.data, form.limite.data)
        flash("Limite alterado com sucesso.", "info")
        return redirect('/cartoes/lista')

    return formulario_limite(form.id.data, form=form)

if __name__ == '__main__':
    app.run(debug=True) 
