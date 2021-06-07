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
    self.acaoPassada = '-1'

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

  def status(self):
    return "Seus Status:\n" + ("Sujo, " if self.sujo else "Limpo, ") + ("Com fome, " if self.fome else "Saciado, ") + (
      "Machucado" if self.machucado else "Saudável\n") + "Energia restante: " + str(
      self.energia) + "\nVidas Restantes: "+ str(self.vidas)+"\n"

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
    if self.get_vidas() > 0:
      return True
    else:
      return False

  def estaComPulgas(self):
    if self.sujeira >= 2:
      return 'Você se sujou mais de uma vez seguida, está com pulgas, isso vai tirar 50 da sua energia por turno sem se lavar'
    else:
      return ''

  def estaMachucado(self):
    if self.machucado == True:
      self.energia -= 100
      self.vidas -= 1
      return 'Você perdeu uma vida e 100 de energia por se machucar mais de uma vez seguida'
    else:
      self.machucado = True
      return ''

  def tomarBanho(self, relogio):
    if self.sujo == True:
      relogio.avancaTempo(30)
      self.sujo = False
      self.sujeira = 0
      if self.sujeira == 2:
        return "Você se sente limpo e livre de pulgas novamente"
      else:
        return "Você se sente limpo"
    else:
      return "Você não está sujo, não precisa se limpar"

  def cacar(self, relogio):
    if self.energia >= 950:
      return ['Você não está com fome para caçar','','']
    else:
      self.ações += 1
      relogio.avancaTempo(30)
      if randint(0, 1000) <= self.energia - 50:
        self.energia += 50
        self.fome = False
        relogio.horasPassadas = 0
        self.acaoPassada = '2'
        return ["Você sucedeu ao caçar sua presa",'','']
      else:
        self.energia -= 100
        return ["Sua presa fugiu, você perdeu 100 de energia por isso.",'','']

  def fazerParkour(self, relogio):
      self.sujeira += 1
      self.ações += 1
      self.sujo = True
      self.energia -= 100
      relogio.avancaTempo(30)
      if randint(0, 1000) <= self.energia - 50:
        self.acaoPassada = '3'
        return ["Você fez altas manobras, os vizinhos acharam até bonito, mas está sujo",self.estaComPulgas(),'']
      else:
        return ['Além de se sujar você também está machucado',self.estaComPulgas(),self.estaMachucado()]

  def voltarParaCasa(self, relogio):
    if self.emCasa == False:
      self.emCasa = True
      relogio.avancaTempo(30)
      return f"Você retornou para casa às {relogio} e realizou {self.ações} ações"
    elif self.emCasa == True:
      return "Você já está em casa"

  def procurarErvas(self, relogio):
    if self.machucado:
      relogio.avancaTempo(30)
      self.energia -= 50
      if randint(0, 10) < 9:
        self.machucado = False
        self.acaoPassada = '7'
        return ['Você achou catnip e melhorou dos problemas de saúde','','']
      else:
        self.sujo = True
        self.sujeira += 1
        return ['Você não achou nada, só perdeu tempo e se sujou',self.estaComPulgas(),'']
    else:
      return ['Você não está machucado!','','']



  def brincar(self, relogio):
    self.energia -= 100
    self.sujo = True
    self.sujeira +=1
    self.ações += 1
    relogio.avancaTempo(30)
    self.acaoPassada = '4'
    if self.sujeira < 2:
      return ["Você se divertiu pra caramba, mas se sujou um pouco!",self.estaComPulgas(),'']
    return ["Você se divertiu, mas esta sujo demais, com pulgas!",self.estaComPulgas(),'']

  # def lutaNoTelhado(self, relogio):
  #   if randint(0, 1000) <= self.energia - 50:
  #     self.estaMachucado()
  #     self.energia -= 50
  #   else:
  #     print("Você triunfou em sua batalha, por isso se sente menos cansado do que antes")
  #     self.energia += 50
  #   self.ações += 1
  #   relogio.avancaTempo(30)
  #
  # def namorar(self, relogio):
  #   if randint(0, 1000) <= self.energia - 50:
  #     self.energia -= 100
  #     print("Seus cortejos não foram bem recebidos, você só se cansou de correr atrás")
  #   else:
  #     self.energia += 50
  #     print("Seus cortejos foram bem recebidos, você se sente renovado.")
  #   relogio.avancaTempo(30)

  def anunciaPersonagem(self):
    print('Você tem que selecionar o personagem')

class PersonagemMacho(Gato):
  def super(self, nome, cor, vidas):
    super.__init__(self, nome, cor, vidas)

  def anunciaPersonagem(self):
    print(f'Você selecionou a jaguatirica {self.nome}.')

  def namorar(self, relogio):
    relogio.avancaTempo(30)
    if randint(0, 1000) <= self.energia-(self.ações):
      self.energia -= 100
      return ["Seus cortejos não foram bem recebidos, você só se cansou de correr atrás -100 de energia",'','','']
    else:
      self.acaoPassada = '6'
      self.energia += 50
      return ["Seus cortejos foram bem recebidos, você se sente renovado +50 de energia.",'','']


  def lutaNoTelhado(self, relogio):
    self.ações += 1
    relogio.avancaTempo(30)
    if randint(0, 1000) <= self.energia - 100:
      self.acaoPassada = '5'
      return ["Você triunfou em sua batalha, sente que não gastou energia",'','']
    else:
      self.energia -= 50
      return ["Você perdeu a luta e se machucou!",'',self.estaMachucado(),'']



class PersonagemFemea(Gato):
  def super(self, nome, cor, vidas):
    Gato.__init__(self, nome, cor, vidas)

  def anunciaPersonagem(self):
    print(f'Você selecionou a gata {self.nome}.')

  def namorar(self, relogio):
    self.ações += 1
    relogio.avancaTempo(30)
    if randint(0, 1000) <= self.energia - 100:
      self.energia -= 100
      return ["Você não gostou do gato que tava afim de você, fugiu dele!",'','','']
    else:
      self.acaoPassada = '6'
      self.energia += 50
      return ["Você arranjou um bom parceiro, esperamos que venha uma ninhada saudável",'','']

  def lutaNoTelhado(self, relogio):
    self.ações += 1
    relogio.avancaTempo(30)
    if randint(0, 1000) <= self.energia-(10*self.ações):
      self.acaoPassada = '5'
      return ["Você triunfou em sua batalha, sente que não gastou energia",'','','5']
    else:
      self.estaMachucado()
      self.energia -= 50
      return ["Você perdeu a luta e se machucou!",'',self.estaMachucado(),'']
