import random

class Jokenpo:
  plays = ["pedra","papel","tesoura"]
  cpu = False
  jogador = False

  def partida(self):
    while True:
      print(f'+{"-"*15}+')
      for i in range(3):
        print(f'│\n')
      
      break

jog1 = Jokenpo()
jog1.partida()
