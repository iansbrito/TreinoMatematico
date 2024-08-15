def rng(max):
    from random import randint
    return [randint(1,max),randint(1,max)]

def verifica_resposta(resp_user, resultado):
    try:
        resultado=float(resultado)
        resp_user = float(resp_user)
        resp_user=round(resp_user,2)
    except ValueError as e:
         return 'Opção invállida'
    if resultado == resp_user:
        return True
    else:
        return False
    
def gera_lista_num(dificuldade):
            if dificuldade =="Fácil":
                num=rng(10)
            if dificuldade == "Médio":
                num=rng(100)
            if dificuldade == "Difícil":
                num=rng(1000)
            return(num)

def gera_operacao(dificuldade,tipo_operacao):
    from operacoes import soma,subtrai, multiplica, divisao
    num = gera_lista_num(dificuldade)
    if tipo_operacao == 'Adição':
        resultado , str_operacao = soma(num)
    if tipo_operacao == 'Subtração':
        resultado, str_operacao = subtrai(num)
    if tipo_operacao == 'Multiplicação':
        resultado, str_operacao = multiplica(num)
    if tipo_operacao == 'Divisão':
        resultado,str_operacao = divisao(num)
        resultado=aproxima_divisao(resultado)
    return resultado, str_operacao

def erro_input(resp_user):
     pass

def aproxima_divisao(resultado):
     aproximado = round(resultado,2)
     return aproximado

