class Carta:
    def __init__(self, tipo: int, valor: int):
        self.tipo = tipo
        self.valor = valor

    #Quantas vezes ambos empataram
    def __eq__(self,other):
        if isinstance(other, Carta):
            return self.valor==other.valor
        raise TypeError("Não é uma Carta válida")

    #Quantas vezes o jogador perdeu ou ganhou
    def __lt__(self,other):
        if isinstance(other, Carta):
            return self.valor<other.valor
        raise TypeError("Não é um Carta válido")

    #Quantas vezes tiraram cartas do mesmo naipe.
    def mesmo_naipe(self,other):
        if isinstance(other, Carta):
            return self.tipo==other.tipo
        raise TypeError("Não é um Carta válido")