from carta import Carta

class Estatistica:
    cartas_jogador = []
    cartas_computador = []
    qtd_vitorias = 0
    qtd_derrotas = 0
    qtd_empates = 0
    qtd_cartas_mesmo_naipe = 0

    def adicionar_cartas(self, carta_jogador: Carta, carta_computador: Carta):
        self.cartas_jogador.append(carta_jogador)
        self.cartas_computador.append(carta_computador)

    def contabilizar_resultado(self):
        for idx, val in enumerate(self.cartas_jogador):
            carta_computador: Carta = self.cartas_computador[idx]
            carta_jogador: Carta = val;
            if carta_jogador.mesmo_naipe(carta_computador):
                self.qtd_cartas_mesmo_naipe = self.qtd_cartas_mesmo_naipe + 1
            elif carta_jogador == carta_computador:
                self.qtd_empates = self.qtd_empates + 1
            elif carta_computador < carta_jogador:
                self.qtd_vitorias = self.qtd_vitorias + 1
            else:
                self.qtd_derrotas = self.qtd_derrotas + 1

    def printar_listas(self):
        print(self.cartas_jogador)
        print(self.cartas_computador)

    def printar_resultado(self):
        print(f'Vitorias', self.qtd_vitorias)
        print(f'Derrotas', self.qtd_derrotas)
        print(f'Empates', self.qtd_empates)
        print(f'Mesmo Naipe', self.qtd_cartas_mesmo_naipe)






    