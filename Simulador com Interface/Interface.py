import tkinter
from tkinter import *
from Relogio import *
from Gatos import *

def tomarBanho(gato, relogio):
    acao = gato.tomarBanho(relogio)
    statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
    resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
    resetaAvisos(acao)
    checkCondicoesDeJogo(gato, relogio)

def cacar(gato, relogio):
    if gato.acaoPassada != '2':
        acao = gato.cacar(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        resetaAvisos(acao)
        checkCondicoesDeJogo(gato, relogio)
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def fazerParkour(gato, relogio):
    if gato.acaoPassada != '3':
        acao = gato.fazerParkour(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        resetaAvisos(acao)
        checkCondicoesDeJogo(gato, relogio)
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def brincar(gato, relogio):
    if gato.acaoPassada != '4':
        acao = gato.brincar(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        resetaAvisos(acao)
        checkCondicoesDeJogo(gato, relogio)
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def lutaNoTelhado(gato, relogio):
    if gato.acaoPassada != '5':
        acao = gato.lutaNoTelhado(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        resetaAvisos(acao)
        checkCondicoesDeJogo(gato, relogio)
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def namorar(gato, relogio):
    if gato.acaoPassada != '6':
        acao = gato.namorar(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        resetaAvisos(acao)
        checkCondicoesDeJogo(gato, relogio)
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def procurarErvas(gato, relogio):
    if gato.acaoPassada != '7':
        acao = gato.procurarErvas(relogio)
        statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
        resultadoDaAcao.configure(text=acao[0], bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
        resetaAvisos(acao)
        checkCondicoesDeJogo(gato, relogio)
    else:
        resultadoDaAcao.configure(text='Não é possível repertir ações bem sucedidas', font=('Helvetice', 15, 'bold'))

def voltarParaCasa(gato, relogio):
    statusDoPersonagem.configure(text=gato.status()+'Horário: '+relogio.horasRestantes())
    resultadoDaAcao.configure(text=gato.voltarParaCasa(relogio), bg='lightblue', fg='black', font=('Helvetice', 15, 'bold'))
    checkCondicoesDeJogo(gato, relogio)
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
    if 22 > relogio.horas >= 6 or not gato.estaVivo():
        if 22 > relogio.horas > 6:
            resultadoDaAcao.configure(text='Você passou muito tempo na rua e o IBAMA te capturou!\nFIM DE JOGO...')
        elif not gato.estaVivo():
            resultadoDaAcao.configure(text=f"Voce perdeu o jogo, {gato.nome} perdeu todas as vidas.")
        avisomachucado.configure(text='', font=('Helvetice', 15))
        avisopulgas.configure(text='', font=('Helvetice', 15))
        disabilitaAcoes()

def checkEnergia(gato, relogio):
    if gato.energia <= 0:
        relogio.avancaTempo(60)
        gato.energia = 100
        avisopulgas.configure(text='Você ficou exausto e cochilou por uma hora!', font=('Helvetice', 15))
        avisomachucado.configure(text='Voltou a ter 100 de energia com este cochilo!', font=('Helvetice', 15))


def resetaAvisos(acao):
    avisopulgas.configure(text=acao[1], font=('Helvetice', 15))
    avisomachucado.configure(text=acao[2], font=('Helvetice', 15))

def criaPersonagem(personagem):
    global gato
    gato = personagem
    global escolha
    escolha = True
    root1.destroy()
    return gato, escolha



if __name__ == "__main__":
    global escolha
    escolha = False
    Mimosa = PersonagemFemea('Mimosa', 'vira-lata', 3)
    Maju = PersonagemFemea('Maju', 'preta', 3)
    Cedrico = PersonagemMacho('Cedrico', 'branco', 3)
    Rumble = PersonagemMacho('Rumble', 'malhado', 3)
    while not escolha:
        root1 = Tk()
        root1.title("Simulador Gaturno")
        root1.geometry("1000x600")
        linhaDaDescricao = Frame(root1)
        linhaDaDescricao.pack(fill=BOTH, expand=True)
        linhaBotoes = Frame(root1)
        linhaBotoes.pack(fill=BOTH, expand=True)
        descricao = Label(linhaDaDescricao, text="Bem vindo ao simulador de noites dos gatos!\nVocê deve sair pela noite realizando atividades felinas.\nNão seja capturado pelo IBAMA nem morra!\n Cada ação tem seu custo de energia, cuide da higiene e saúde do seu personagem.\n Ao voltar para dormir, se o personagem ainda estiver vivo o jogo encerrará!\nEscolha um dos personagens abaixo:",bg='white', fg='black', font=('Helvetice', 20, 'bold'))
        descricao.pack(expand=True, fill=BOTH)
        descricao.bind('<Configure>', lambda e: descricao.config(wraplength=descricao.winfo_width()))
        btnMimosa = Button(linhaBotoes, text = "Mimosa", command = lambda: criaPersonagem(Mimosa), font=('Helvetice', 15, 'bold'))
        btnMimosa.pack(fill=BOTH, expand=True)
        btnMaju = Button(linhaBotoes, text = "Maju", command = lambda: criaPersonagem(Maju), font=('Helvetice', 15, 'bold'))
        btnMaju.pack(fill=BOTH, expand=True)
        btnCedrico = Button(linhaBotoes, text = "Cedrico", command = lambda: criaPersonagem(Cedrico), font=('Helvetice', 15, 'bold'))
        btnCedrico.pack(fill=BOTH, expand=True)
        btnRumble = Button(linhaBotoes, text = "Rumble", command = lambda: criaPersonagem(Rumble), font=('Helvetice', 15, 'bold'))
        btnRumble.pack(fill=BOTH, expand=True)
        btnAct0 = Button(linhaBotoes, text="Sair do jogo", command=lambda: sair(), font=('Helvetice', 15, 'bold'))
        btnAct0.pack(fill=BOTH, expand=True)
        root1.mainloop()
    root = Tk()
    root.title("Simulador Gaturno")
    root.geometry("800x800")
    relogio = Relogio()
    linhaeq = Frame(root)
    linhaeq.pack(fill=BOTH, expand=True)
    linhaBtn = Frame(linhaeq).pack()
    global resultadoDaAcao
    resultadoDaAcao = Label(root)
    global avisopulgas
    avisopulgas = Label(root)
    global avisomachucado
    avisomachucado = Label(root)
    global statusDoPersonagem
    statusDoPersonagem = Label(linhaeq, text = gato.status()+'Horário: '+relogio.horasRestantes(), bg='yellow', fg='black', font=('Helvetice', 20, 'bold'))
    statusDoPersonagem.pack(fill=BOTH, expand=True)
    btnAct1 = Button(linhaBtn, text = "Se lavar [30 min, 0 energia]", command = lambda: tomarBanho(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct1.pack(fill=BOTH, expand=True)
    btnAct2 = Button(linhaBtn, text = "Caçar [30 min, 100 energia]", command = lambda: cacar(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct2.pack(fill=BOTH, expand=True)
    btnAct3 = Button(linhaBtn, text = "Fazer parkour [30 min, 100 energia]", command = lambda: fazerParkour(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct3.pack(fill=BOTH, expand=True)
    btnAct4 = Button(linhaBtn, text = "Brincar [30 min, 100 energia]", command = lambda: brincar(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct4.pack(fill=BOTH, expand=True)
    btnAct5 = Button(linhaBtn, text = "Luta no telhado [30 min, 50 energia]", command = lambda: lutaNoTelhado(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct5.pack(fill=BOTH, expand=True)
    btnAct6 = Button(linhaBtn, text = "Namorar [30 min, 50 energia]", command = lambda: namorar(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct6.pack(fill=BOTH, expand=True)
    btnAct7 = Button(linhaBtn, text = "Procurar ervas para se medicar", command = lambda: procurarErvas(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct7.pack(fill=BOTH, expand=True)
    btnAct8 = Button(linhaBtn, text = "Voltar para dormir", command = lambda: voltarParaCasa(gato, relogio),font=('Helvetice', 15, 'bold'))
    btnAct8.pack(fill=BOTH, expand=True)
    btnAct0 = Button(linhaBtn, text = "Sair do jogo", command = lambda: sair(),font=('Helvetice', 15, 'bold'))
    btnAct0.pack(fill=BOTH, expand=True)
    resultadoDaAcao.pack(fill=BOTH, expand=True)
    avisopulgas.pack(fill=BOTH, expand=True)
    avisomachucado.pack(fill=BOTH, expand=True)
    root.mainloop()

