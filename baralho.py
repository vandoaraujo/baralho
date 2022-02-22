#O módulo random tem o método shuffle que embaralha
# elementos de uma lista python, trocando sua ordem,
# portanto, pode ser usado em uma classe “Baralho”
# para justamente embaralhar as cartas.
import random

from carta import Carta

class Baralho:
    def __init__(self):
        self.cartas = []
        for tipo in range(4):
            for valor in range(1, 14):
                carta = Carta(tipo, valor)
                self.cartas.append(carta)

    def embaralhar(self):
         random.shuffle(self.cartas)

    def retirar_carta(self):
        if len(self.cartas) != 0:
            return self.cartas.pop()
        return None
        
