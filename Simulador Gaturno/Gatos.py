from random import randint
from time import sleep
class Gato:
  def __init__(self, nome, cor, vidas):
    self.nome = nome
    self.cor = cor
    self.__vidas = vidas
    self.sujo = False
    self.fome = False
    self.machucado = False
    self.energia = 1000
    self.emCasa = False
    self.ações = 0
    self.sujeira = 0
    self.açãoPassada = '-1'

  def get_vidas(self):
      return self.__vidas

  def set_vidas(self, vidas):
      self.__vidas = vidas

  @property
  def vidas(self):
      return self.__vidas

  @vidas.setter
  def vidas(self, vidas):
    self.__vidas = vidas

  def __str__(self):
    return "Você está " + ("sujo" if self.sujo else "limpo") + ", " + ("com" if self.fome else "sem") + " fome e " + (
        "mal de saúde" if self.machucado else "bem de saúde") + ". Você tem " + str(
        self.energia) + " de energia para consumir."

  def temEnergia(self, energiaNecessaria):
    if self.energia >= energiaNecessaria:
      return True
    else:
      return False

  def estaVivo(self):
    if self.vidas > 0:
      return True
    else:
      return False

  def estaComPulgas(self):
    if self.sujeira >= 2:
      print('Você se sujou mais de uma vez seguida, está com pulgas, isso vai tirar 50 da sua energia por turno sem se lavar')


  def tomarBanho(self, relogio):
    if self.sujo == True:
      relogio.avancaTempo(30)
      self.sujo = False
      self.sujeira = 0
      if self.sujeira == 2:
        print("Você se sente limpo e livre de pulgas novamente")
      else:
        print("Você se sente limpo")
    else:
      print("Você não está sujo, não precisa se limpar")

  def estaMachucado(self):
    if self.machucado == True:
      self.energia -= 100
      self.vidas -= 1
      print('Você perdeu uma vida por se machucar mais de uma vez seguida')
      print('\n')
      sleep(1)
    else:
      self.energia -= 50
      self.machucado = True
      print('\n')
      sleep(1)

  def cacar(self, relogio):
    if self.energia >= 950:
      print('Você não está com fome para caçar')
      print('\n')
      sleep(1)
    elif not self.temEnergia(100):
      print('Você não tem energia para executar esta ação')
      print('\n')
      sleep(1)
    else:
      if randint(0, 1000) <= self.energia - 50:
        self.energia += 50
        print("Você sucedeu ao caçar sua presa")
        print('\n')
        sleep(1)
        self.fome = False
        self.açãoPassada = '2'
        relogio.horasPassadas = 0
      else:
        print("Sua presa fugiu, você perdeu 100 de energia por isso.")
        print('\n')
        sleep(1)
        self.energia -= 100
      self.ações += 1
      relogio.avancaTempo(30)

  def voltarParaCasa(self, relogio):
    if self.emCasa == False:
      self.emCasa = True
      relogio.avancaTempo(30)
      print("Você retornou para casa às", relogio, " e realizou", self.ações, " ações")
      sleep(1)
      exit()
    elif self.emCasa == True:
      print("Você já está em casa")
      print('\n')
      sleep(1)

  def procurarErvas(self, relogio):
    if self.machucado:
      if randint(0, 10) < 9:
        print('Você achou catnip e melhorou dos problemas de saúde')
        print('\n')
        sleep(1)
        self.machucado = False
        self.açãoPassada = '8'
      else:
        print('Você não achou nada, só perdeu tempo e se sujou')
        self.sujo = True
        self.sujeira += 1
        self.estaComPulgas()
        print('\n')
        sleep(1)
      self.energia -= 50
      relogio.avancaTempo(30)
    else:
      print('Você não está machucado!')
      print('\n')
      sleep(1)

  def fazerParkour(self, relogio):
    if not self.temEnergia(50):
      print('Você não tem energia para executar esta ação')
      print('\n')
      sleep(1)
    else:
      if randint(0, 1000) <= self.energia - 50:
        self.energia -= 100
        print("Você fez altas manobras, os vizinhos acharam até bonito, mas está sujo")
        self.sujo = True
        self.sujeira += 1
        self.estaComPulgas()
        print('\n')
        self.açãoPassada = '3'
        sleep(1)
        self.ações += 2
        relogio.avancaTempo(30)
      else:
        self.energia -= 150
        self.estaMachucado()
        self.sujo = True
        self.sujeira += 1
        self.estaComPulgas()
        print('Além de se machucar você também está sujo')
        self.ações += 1
        relogio.avancaTempo(30)


  def brincar(self, relogio):
    self.energia -= 100
    self.sujo = True
    self.sujeira +=1
    self.estaComPulgas()
    if self.sujeira < 2:
      print("Você se divertiu e agora está sujo, se lave para não arriscar pegar pulgas!")
    print('\n')
    sleep(1)
    self.ações += 1
    if randint(0, 10) > 8:
      self.ações += 1
    self.açãoPassada = '4'
    relogio.avancaTempo(30)

  def lutaNoTelhado(self, relogio):
    if randint(0, 1000) <= self.energia - 50:
      self.estaMachucado()
      self.energia -= 50
    else:
      print("Você triunfou em sua batalha, por isso se sente menos cansado do que antes")
      print('\n')
      sleep(1)
      self.energia += 50
    self.ações += 1
    relogio.avancaTempo(30)

  def namorar(self, relogio):
    if randint(0, 1000) <= self.energia - 50:
      self.energia -= 100
      print("Seus cortejos não foram bem recebidos, você só se cansou de correr atrás")
      print('\n')
      sleep(1)
    else:
      self.energia += 50
      print("Seus cortejos foram bem recebidos, você se sente renovado.")
      print('\n')
      sleep(1)
    relogio.avancaTempo(30)

  def anunciaPersonagem(self):
    print('Você tem que selecionar o personagem')

class PersonagemMacho(Gato):
  def super(self, nome, cor, vidas):
    super.__init__(self, nome, cor, vidas)

  def anunciaPersonagem(self):
    print(f'Você selecionou a jaguatirica {self.nome}.')

  def namorar(self, relogio):
    if randint(0, 1000) <= self.energia-(self.ações):
      self.energia -= 100
      print("Seus cortejos não foram bem recebidos, você só se cansou de correr atrás")
      print('\n')
      sleep(1)
    else:
      self.energia += 50
      print("Seus cortejos foram bem recebidos, você se sente renovado.")
      print('\n')
      sleep(1)
      self.açãoPassada = '6'
    relogio.avancaTempo(30)

  def lutaNoTelhado(self, relogio):
    if randint(0, 1000) <= self.energia - 100:
      print("Você triunfou em sua batalha, sente que não gastou energia")
      print('\n')
      sleep(1)
      self.açãoPassada = '5'
    else:
      self.estaMachucado()
      self.energia -= 50
      print("Você perdeu a luta e se machucou!")
    self.ações += 1
    relogio.avancaTempo(30)


class PersonagemFemea(Gato):
  def super(self, nome, cor, vidas):
    Gato.__init__(self, nome, cor, vidas)

  def anunciaPersonagem(self):
    print(f'Você selecionou a gata {self.nome}.')

  def namorar(self, relogio):
    if randint(0, 1000) <= self.energia - 100:
      self.energia -= 100
      print("Você não gostou do gato que tava afim de você, fugiu dele!")
      print('\n')
      sleep(1)
    else:
      self.energia += 50
      print("Você arranjou um bom parceiro, esperamos que venha uma ninhada saudável")
      print('\n')
      sleep(1)
      self.açãoPassada = '6'
    relogio.avancaTempo(30)

  def lutaNoTelhado(self, relogio):
    if randint(0, 1000) <= self.energia-(10*self.ações):
      print("Você triunfou em sua batalha, sente que não gastou energia")
      print('\n')
      sleep(1)
      self.açãoPassada = '5'
    else:
      self.estaMachucado()
      self.energia -= 50
      print("Você perdeu a luta e se machucou!")
    self.ações += 1
    relogio.avancaTempo(30)