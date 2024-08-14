from flask import Flask,render_template,redirect,request, url_for
from utilidades import gera_operacao, verifica_resposta

app=Flask(__name__)

#DEFINE OPERAÇÃO<-----------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/define_operacao', methods=['GET', 'POST'])
def define_operacao():
    return render_template('define_operacao.html')
#DEFINE DIFICULDADE<------------------------------------------------------------------------
@app.route('/define_dificuldade', methods=['GET','POST'])
def define_dificuldade():
    try:
        if request.form['operacao']:
            operacao = request.form['operacao']
            return render_template('define_dificuldade.html', operacao=operacao)
    except (KeyError, TypeError) as e:
            return redirect(url_for('define_operacao'))

#REALIZA OPERAÇÃO<------------------------------------------------------------------------------------------
@app.route('/realizar_operacao', methods=['GET','POST'])
def realizar_operacao():
    from utilidades import rng,verifica_resposta
    try:
        if (request.form['operacao'], request.form['dificuldade']):
            tipo_operacao=request.form['operacao']
            dificuldade = request.form['dificuldade']
            resultado , str_operacao = gera_operacao(dificuldade,tipo_operacao)


            return render_template('realizar_operacao.html', operacao=tipo_operacao, dificuldade=dificuldade,str_operacao=str_operacao ,resultado=resultado)
    except (KeyError, TypeError):
        return redirect(url_for('define_operacao'))

#VERIFICA RESPOSTA<----------------------------------------------------------------------------------------
@app.route('/resultado_operacao', methods=['GET', 'POST'])
def resultado_operacao():
    resultado = request.form['resultado']
    resposta_user = request.form['resposta_usuario']
    if verifica_resposta(resposta_user,resultado) == True:
        msg='Parabéns, você acertou!'
    else:
        msg = 'Você errou, tente novamente!'
    print(resultado)
    return render_template('resultado_operacao.html', msg=msg)
    
#FINALIZA PROGRAMA<-------------------------------------------------------------------------------------------
if __name__ == "__main__":  
    app.run(debug=True)