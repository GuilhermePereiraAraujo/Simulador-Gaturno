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

    def horasRestantes(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        if(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
            self.horasPassadas += 1
        if self.horas == 24:
            self.horas = 0
       