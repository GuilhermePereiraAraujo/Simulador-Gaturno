# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas, entre outros.
# O código apresentado abaixo é apenas um modelo a ser utilizado como referência. O Grupo pode criar uma nova situação e inclusive melhorar o código abaixo.
from random import randint
from time import sleep
from Gatos import *
class Relogio:
    def __init__(self):
        self.horas = 22
        self.minutos = 0
        self.horasPassadas = 0

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        if(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
            self.horasPassadas += 1
        if self.horas == 24:
            self.horas = 0



if(__name__ == "__main__"):
    print("Bem vindo ao simulador de noites dos gatos, neste jogo você tem como objetivo, perambular pela noite realizando atividades felinas sem se exaurir e sem se machucar para não ser capturado pelo IBAMA ou falecer!")
    print('Cada ação tem seu custo de energia e tempo, cuide da higiene e saúde do seu personagem')
    print("As ações [3 - Fazer parkour] e [4 - Brincar] tem possibilidade de contar ações extras, mas são mais caras e arriscadas")
    print('Ao selecionar a opção [8 - Voltar para dormir], se o personagem ainda estiver vivo o jogo encerrará')
    print('1 - Maju')
    print('2 - Cedrico')
    per = int(input("Selecione um personagem:"))
    print('\n')
    if per == 1:
        gato = PersonagemFemea('Maju', 'preta', 3)
    elif per == 2:
        gato = PersonagemMacho('Cedrico', 'branca', 3)
    gato.anunciaPersonagem()
    sleep(0.5)
    relogio = Relogio()
    while True:
            if gato.energia <= 0:
                print("Você ficou exausto e precisou tirar uma soneca de 30 min para recuperar 100 de energia!")
                sleep(1)
                gato.energia += 100
                relogio.avancaTempo(30)

            if 22 > relogio.horas >=6:
                print('Você passou muito tempo na rua e o IBAMA te capturou!')
                print('FIM DE JOGO...')
                break

            if relogio.horasPassadas > 3 and gato.fome == False:
                gato.fome = True
                print("Você está com fome, vai perder 50 de energia por turno se não comer")
                print('\n')
                sleep(1)

            if not gato.estaVivo():
                print(f"Voce perdeu o jogo, {gato.nome} perdeu todas as vidas.")
                print('\n')
                sleep(1)
                break

            print("---------")
            sleep(0.5)
            print("São "+str(relogio)+" horas, você tem que voltar para a casa antes que te descubram (6:00) e realizando o maior numero de atividades possível sem morrer.")
            sleep(0.5)
            print(gato)
            sleep(0.5)
            print("---------\nAções:")
            sleep(0.5)
            print("Ação - Descrição [Requisitos Mínimos]")
            print("1 - Se lavar [30 min, 0 energia]")
            print("2 - Caçar [30 min, 100 energia]")
            print("3 - Fazer parkour [30 min, 100 energia]")
            print("4 - Brincar [30 min, 100 energia]")
            print("5 - Luta no telhado [30 min, 50 energia]")
            print("6 - Namorar [30 min, 50 energia]")
            print("7 - Procurar ervas para se medicar")
            print("8 - Voltar para dormir ")
            print("0 - Sair do jogo")
            sleep(0.5)

            opcao = input("Escolha sua ação:")
            if opcao in ('1','2','3','4','5','6','7','8','0') and opcao != gato.açãoPassada:
                if(opcao == "1"):
                    gato.tomarBanho(relogio)
                elif(opcao == "2"):
                    gato.cacar(relogio)
                elif(opcao == "3"):
                    gato.fazerParkour(relogio)
                elif(opcao == "4"):
                    gato.brincar(relogio)
                elif(opcao == "5"):
                    gato.lutaNoTelhado(relogio)
                elif(opcao == "6"):
                    gato.namorar(relogio)
                elif(opcao == "7"):
                    gato.procurarErvas(relogio)
                elif(opcao == "8"):
                    gato.voltarParaCasa(relogio)
                elif(opcao == "0"):
                    break
                if gato.sujeira >= 2:
                    gato.energia -= 50
                    print('Tome banho para se livrar das pulgas!')
                if gato.fome == True:
                    gato.energia -= 50
            elif opcao == gato.açãoPassada:
                print("Você não pode repetir ações bem sucedidas")
            else:
                print("Opção inválida! Digite uma opção entre 0 e 8!")
                sleep(0.5)
                print('\n')

       