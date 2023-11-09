from flask import Flask, request, render_template, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
from util import answers
from util import db

app = Flask(__name__)

items_per_page = 5

@app.route('/bot', methods = ['POST'])
def bot():
    answer = answers.firstAnswer()
    return answer
@app.route('/')
def pagina_inicial():
    return render_template('pagina_inicial.html', menu_expandido=False)

@app.route('/error')
def error():
    return render_template('error.html', menu_expandido=False)

@app.route('/adcatacado', methods=['GET', 'POST'])
def adcatacado():
    if request.method == 'POST':
        texto = request.form['texto']
        telefone = request.form['telefone']

        if db.BuscarAtacadoNome(texto) == False and db.BuscarAtacadoTel(telefone) == False:
            db.newAtacado(texto, telefone)
            atacado()
            return redirect(url_for('atacado'))
        else:
            return redirect(url_for('error'))
    return render_template('adcatacado.html', menu_expandido=False)

@app.route('/adcvarejo', methods=['GET', 'POST'])
def adcvarejo():
    if request.method == 'POST':
        texto = request.form['texto']
        telefone = request.form['telefone']

        if db.BuscarVarejoNome(texto) == False and db.BuscarVarejoTel(telefone) == False:
            db.newVarejo(texto, telefone)
            varejo()
            return redirect(url_for('varejo'))
        else:
            return redirect(url_for('error'))
    return render_template('adcvarejo.html', menu_expandido=False)

@app.route('/adcgerencia', methods=['GET', 'POST'])
def adcgerencia():
    if request.method == 'POST':
        texto = request.form['texto']
        telefone = request.form['telefone']

        if db.BuscarGerenteNome(texto) == False and db.BuscarGerenteTel(telefone) == False:
            db.newGerente(texto, telefone)
            gerencia()
            return redirect(url_for('gerencia'))
        else:
            return redirect(url_for('error'))
    return render_template('adcgerencia.html', menu_expandido=False)

@app.route('/adcsetor_de_compras', methods=['GET', 'POST'])
def adcsetor_de_compras():
    if request.method == 'POST':
        texto = request.form['texto']
        telefone = request.form['telefone']

        if db.BuscarSetorDeComprasNome(texto) == False and db.BuscarSetorDeComprasTel(telefone) == False:
            db.newSetorDeCompras(texto, telefone)
            setor_de_compras()
            return redirect(url_for('setor_de_compras'))
        else:
            return redirect(url_for('error'))
    return render_template('adcsetor_de_compras.html', menu_expandido=False)

@app.route('/adcsac', methods=['GET', 'POST'])
def adcsac():
    if request.method == 'POST':
        texto = request.form['texto']
        telefone = request.form['telefone']

        if db.BuscarSacNome(texto) == False and db.BuscarSacTel(telefone) == False:
            db.newSac(texto, telefone)
            sac()
            return redirect(url_for('sac'))
        else:
            return redirect(url_for('atacado'))
    return render_template('adcsac.html', menu_expandido=False)

@app.route('/delatacado', methods=['GET', 'POST'])
def delatacado():
    lista_aux = db.listarAtacado()
    lista_elementos = list()

    for elemento in lista_aux:
        lista_elementos.append(elemento[1])

    if request.method == 'POST':
        elemento_selecionado = request.form['elemento']
        db.deleteAtacado(elemento_selecionado)
        return redirect(url_for('atacado'))
    return render_template('delatacado.html', menu_expandido=False, lista_elementos=lista_elementos)

@app.route('/delvarejo', methods=['GET', 'POST'])
def delvarejo():
    lista_aux = db.listarVarejo()
    lista_elementos = list()

    for elemento in lista_aux:
        lista_elementos.append(elemento[1])

    if request.method == 'POST':
        elemento_selecionado = request.form['elemento']
        db.deleteVarejo(elemento_selecionado)
        return redirect(url_for('varejo'))
    return render_template('delvarejo.html', menu_expandido=False, lista_elementos=lista_elementos)

@app.route('/delgerencia', methods=['GET', 'POST'])
def delgerencia():
    lista_aux = db.listarGerente()
    lista_elementos = list()

    for elemento in lista_aux:
        lista_elementos.append(elemento[1])

    if request.method == 'POST':
        elemento_selecionado = request.form['elemento']
        db.deleteGerente(elemento_selecionado)
        return redirect(url_for('gerencia'))
    return render_template('delgerencia.html', menu_expandido=False, lista_elementos=lista_elementos)

@app.route('/delsetor_de_compras', methods=['GET', 'POST'])
def delsetor_de_compras():
    lista_aux = db.listarSetorDeCompras()
    lista_elementos = list()

    for elemento in lista_aux:
        lista_elementos.append(elemento[1])

    if request.method == 'POST':
        elemento_selecionado = request.form['elemento']
        db.deleteSetorDeCompras(elemento_selecionado)
        return redirect(url_for('setor_de_compras'))
    return render_template('delsetor_de_compras.html', menu_expandido=False, lista_elementos=lista_elementos)

@app.route('/delsac', methods=['GET', 'POST'])
def delsac():
    lista_aux = db.listarSac()
    lista_elementos = list()

    for elemento in lista_aux:
        lista_elementos.append(elemento[1])

    if request.method == 'POST':
        elemento_selecionado = request.form['elemento']
        db.deleteSac(elemento_selecionado)
        return redirect(url_for('sac'))
    return render_template('delsac.html', menu_expandido=False, lista_elementos=lista_elementos)

@app.route('/atacado')
def atacado():

    data_list = db.listarAtacado()

    page = int(request.args.get('page', 1))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    items_to_display = data_list[start_index:end_index]
    num_pages = (len(data_list) // items_per_page + 1)
    return render_template('atacado.html', menu_expandido=False, items=items_to_display, page=page, num_pages=num_pages)

@app.route('/varejo')
def varejo():
    data_list = db.listarVarejo()
    page = int(request.args.get('page', 1))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    items_to_display = data_list[start_index:end_index]
    num_pages = (len(data_list) // items_per_page + 1)
    return render_template('varejo.html', menu_expandido=False, items=items_to_display, page=page, num_pages=num_pages)

@app.route('/setor_de_compras')
def setor_de_compras():
    data_list = db.listarSetorDeCompras()
    page = int(request.args.get('page', 1))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    items_to_display = data_list[start_index:end_index]
    num_pages = (len(data_list) // items_per_page + 1)
    return render_template('setor_de_compras.html', menu_expandido=False, items=items_to_display, page=page, num_pages=num_pages)

@app.route('/gerencia')
def gerencia():
    data_list = db.listarGerente()
    page = int(request.args.get('page', 1))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    items_to_display = data_list[start_index:end_index]
    num_pages = (len(data_list) // items_per_page + 1)
    return render_template('gerencia.html', menu_expandido=False, items=items_to_display, page=page, num_pages=num_pages)

@app.route('/sac')
def sac():
    data_list = db.listarSac()
    page = int(request.args.get('page', 1))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    items_to_display = data_list[start_index:end_index]
    num_pages = (len(data_list) // items_per_page + 1)
    return render_template('sac.html', menu_expandido=False, items=items_to_display, page=page, num_pages=num_pages)

if __name__ == '__main__':
    app.run()