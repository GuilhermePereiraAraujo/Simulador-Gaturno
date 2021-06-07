from tkinter import *
from Relogio import *
from Gatos import *

def tomarBanho(gato, relogio):
    acao = gato.tomarBanho(relogio)
    statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
    resultadoDaAcao.configure(text= acao,bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
    avisopulgas.configure(text='', font=('Helvetice', 15))
    avisomachucado.configure(text='', font=('Helvetice', 15))
    avisopulgas.configure(text='', font=('Helvetice', 15))
    if checkCondicoesDeJogo(gato, relogio) != '':
        resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
        disabilitaAcoes()

def cacar(gato, relogio):
    if gato.acaoPassada != '2':
        acao = gato.cacar(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0],bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        if acao[1] != '':
            avisopulgas.configure(text = acao[1], font=('Helvetice', 15))
        if acao[2] != '':
            avisomachucado.configure(text = acao[2], font=('Helvetice', 15))
        else:
            avisomachucado.configure(text='', font=('Helvetice', 15))
        if checkCondicoesDeJogo(gato, relogio) != '':
            resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
            disabilitaAcoes()
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def fazerParkour(gato, relogio):
    if gato.acaoPassada != '3':
        acao = gato.fazerParkour(relogio)
        statusDoPersonagem.configure(text = gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text = acao[0],bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        if acao[1] != '':
            avisopulgas.configure(text = acao[1], font=('Helvetice', 15))
        if acao[2] != '':
            avisomachucado.configure(text = acao[2], font=('Helvetice', 15))
        else:
            avisomachucado.configure(text='', font=('Helvetice', 15))
        if checkCondicoesDeJogo(gato, relogio) != '':
            resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
            disabilitaAcoes()
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def brincar(gato, relogio):
    if gato.acaoPassada != '4':
        acao = gato.brincar(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0],bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        if acao[1] != '':
            avisopulgas.configure(text=acao[1], font=('Helvetice', 15))
        if acao[2] != '':
            avisomachucado.configure(text=acao[2], font=('Helvetice', 15))
        else:
            avisomachucado.configure(text='', font=('Helvetice', 15))
        if checkCondicoesDeJogo(gato, relogio) != '':
            resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
            disabilitaAcoes()
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def lutaNoTelhado(gato, relogio):
    if gato.acaoPassada != '5':
        acao = gato.lutaNoTelhado(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0],bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        if acao[1] != '':
            avisopulgas.configure(text=acao[1], font=('Helvetice', 15))
        if acao[2] != '':
            avisomachucado.configure(text=acao[2], font=('Helvetice', 15))
        else:
            avisomachucado.configure(text='', font=('Helvetice', 15))
        if checkCondicoesDeJogo(gato, relogio) != '':
            resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
            disabilitaAcoes()
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def namorar(gato, relogio):
    if gato.acaoPassada != '6':
        acao = gato.namorar(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0],bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        if acao[1] != '':
            avisopulgas.configure(text=acao[1], font=('Helvetice', 15))
        if acao[2] != '':
            avisomachucado.configure(text=acao[2], font=('Helvetice', 15))
        else:
            avisomachucado.configure(text='', font=('Helvetice', 15))
        if checkCondicoesDeJogo(gato, relogio) != '':
            resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
            disabilitaAcoes()
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def procurarErvas(gato, relogio):
    if gato.acaoPassada != '7':
        acao = gato.procurarErvas(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0],bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        if acao[1] != '':
            avisopulgas.configure(text=acao[1], font=('Helvetice', 15))
        if not gato.machucado:
            avisomachucado.configure(text='', font=('Helvetice', 15))
        if checkCondicoesDeJogo(gato, relogio) != '':
            resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
            disabilitaAcoes()
            avisomachucado.configure(text='', font=('Helvetice', 15))
            avisopulgas.configure(text='', font=('Helvetice', 15))
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def voltarParaCasa(gato, relogio):
    statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
    resultadoDaAcao.configure(text=gato.voltarParaCasa(relogio),bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
    if checkCondicoesDeJogo(gato, relogio) != '':
        resultadoDaAcao.configure(text = checkCondicoesDeJogo(gato, relogio))
    disabilitaAcoes()

def sair():
    exit()

def disabilitaAcoes():
    btnAct1.configure(state=DISABLED)
    btnAct2.configure(state=DISABLED)
    btnAct3.configure(state=DISABLED)
    btnAct4.configure(state=DISABLED)
    btnAct5.configure(state=DISABLED)
    btnAct6.configure(state=DISABLED)
    btnAct7.configure(state=DISABLED)
    btnAct8.configure(state=DISABLED)

def checkCondicoesDeJogo(gato, relogio):
    if gato.sujeira >= 2:
        gato.energia -= 50
    if gato.fome == True:
        gato.energia -= 50
    if 22 > relogio.horas >= 6:
        return 'Você passou muito tempo na rua e o IBAMA te capturou!\nFIM DE JOGO...'
    elif not gato.estaVivo():
        return f"Voce perdeu o jogo, {gato.nome} perdeu todas as vidas."
    else:
        return ''

relogio = Relogio()
gato = PersonagemFemea('Mimosa', 'vira-lata', 3)
root = Tk()
root.title("Simulador Gaturno")
root.geometry("1200x900")
linhaeq = Frame(root)
linhaeq.pack(fill=BOTH, expand=True)
linhaBtn = Frame(linhaeq).pack()
linhaResp = Frame(linhaeq).pack()
resultadoDaAcao = Label(root)
avisopulgas = Label(root)
avisomachucado = Label(root)
statusDoPersonagem = Label(linhaeq, text = gato.status()+'Horário: '+relogio.horasRestantes(), bg='yellow', fg='black', font=('Helvetice', 20, 'bold'))
statusDoPersonagem.pack(fill=BOTH, expand=True)
btnAct1 = Button(linhaBtn, text = "1 - Se lavar [30 min, 0 energia]", command = lambda: tomarBanho(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct1.pack(fill=BOTH, expand=True)
btnAct2 = Button(linhaBtn, text = "2 - Caçar [30 min, 100 energia]", command = lambda: cacar(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct2.pack(fill=BOTH, expand=True)
btnAct3 = Button(linhaBtn, text = "3 - Fazer parkour [30 min, 100 energia]", command = lambda: fazerParkour(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct3.pack(fill=BOTH, expand=True)
btnAct4 = Button(linhaBtn, text = "4 - Brincar [30 min, 100 energia]", command = lambda: brincar(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct4.pack(fill=BOTH, expand=True)
btnAct5 = Button(linhaBtn, text = "5 - Luta no telhado [30 min, 50 energia]", command = lambda: lutaNoTelhado(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct5.pack(fill=BOTH, expand=True)
btnAct6 = Button(linhaBtn, text = "6 - Namorar [30 min, 50 energia]", command = lambda: namorar(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct6.pack(fill=BOTH, expand=True)
btnAct7 = Button(linhaBtn, text = "7 - Procurar ervas para se medicar", command = lambda: procurarErvas(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct7.pack(fill=BOTH, expand=True)
btnAct8 = Button(linhaBtn, text = "8 - Voltar para dormir", command = lambda: voltarParaCasa(gato, relogio),font=('Helvetice', 15, 'bold'))
btnAct8.pack(fill=BOTH, expand=True)
btnAct0 = Button(linhaBtn, text = "0 - Sair do jogo", command = lambda: sair(),font=('Helvetice', 15, 'bold'))
btnAct0.pack(fill=BOTH, expand=True)
resultadoDaAcao.pack(fill=BOTH, expand=True)
avisopulgas.pack(fill=BOTH, expand=True)
avisomachucado.pack(fill=BOTH, expand=True)
root.mainloop()
